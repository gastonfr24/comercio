"""
Tests for products app.
"""
from decimal import Decimal
import pytest
from django.core.exceptions import ValidationError
from apps.products.models import Product


@pytest.mark.django_db
class TestProductModel:
    """Tests for Product model."""

    def test_create_product(self):
        """Test creating a product with valid data."""
        product = Product.objects.create(
            barcode="1234567890",
            name="Test Product",
            price=Decimal("10.00"),
            cost=Decimal("5.00"),
            stock=100,
            category="Test Category",
        )

        assert product.id is not None
        assert product.barcode == "1234567890"
        assert product.name == "Test Product"
        assert product.price == Decimal("10.00")
        assert product.cost == Decimal("5.00")
        assert product.stock == 100
        assert product.is_active is True

    def test_product_str_representation(self):
        """Test string representation of product."""
        product = Product.objects.create(
            barcode="ABC123",
            name="Sample Product",
            price=Decimal("15.00"),
        )

        assert str(product) == "Sample Product (ABC123)"

    def test_barcode_normalization(self):
        """Test that barcode is normalized to uppercase."""
        product = Product.objects.create(
            barcode="abc123xyz",
            name="Test Product",
            price=Decimal("10.00"),
        )

        assert product.barcode == "ABC123XYZ"

    def test_barcode_uniqueness(self):
        """Test that barcode must be unique."""
        Product.objects.create(
            barcode="UNIQUE123",
            name="Product 1",
            price=Decimal("10.00"),
        )

        with pytest.raises(Exception):  # IntegrityError
            Product.objects.create(
                barcode="UNIQUE123",
                name="Product 2",
                price=Decimal("20.00"),
            )

    def test_price_cannot_be_lower_than_cost(self):
        """Test validation that price must be >= cost."""
        with pytest.raises(ValidationError) as exc_info:
            Product.objects.create(
                barcode="TEST001",
                name="Invalid Product",
                price=Decimal("5.00"),
                cost=Decimal("10.00"),
            )

        assert "price" in exc_info.value.error_dict

    def test_profit_margin_calculation(self):
        """Test profit margin calculation."""
        product = Product.objects.create(
            barcode="TEST002",
            name="Margin Test",
            price=Decimal("75.00"),
            cost=Decimal("50.00"),
            stock=10,
        )

        # (75 - 50) / 50 * 100 = 50%
        assert product.profit_margin == Decimal("50.00")

    def test_profit_margin_with_zero_cost(self):
        """Test profit margin when cost is zero."""
        product = Product.objects.create(
            barcode="TEST003",
            name="Zero Cost",
            price=Decimal("10.00"),
            cost=Decimal("0.00"),
            stock=5,
        )

        assert product.profit_margin == Decimal("0.00")

    def test_in_stock_property(self):
        """Test in_stock property."""
        product_in_stock = Product.objects.create(
            barcode="IN001",
            name="In Stock",
            price=Decimal("10.00"),
            stock=5,
        )

        product_out_of_stock = Product.objects.create(
            barcode="OUT001",
            name="Out of Stock",
            price=Decimal("10.00"),
            stock=0,
        )

        assert product_in_stock.in_stock is True
        assert product_out_of_stock.in_stock is False

    def test_decrease_stock(self):
        """Test decreasing product stock."""
        product = Product.objects.create(
            barcode="STOCK001",
            name="Stock Test",
            price=Decimal("10.00"),
            stock=10,
        )

        product.decrease_stock(3)
        assert product.stock == 7

        product.decrease_stock(7)
        assert product.stock == 0

    def test_decrease_stock_insufficient(self):
        """Test that decreasing stock below zero raises error."""
        product = Product.objects.create(
            barcode="STOCK002",
            name="Low Stock",
            price=Decimal("10.00"),
            stock=5,
        )

        with pytest.raises(ValidationError) as exc_info:
            product.decrease_stock(10)

        assert "Insufficient stock" in str(exc_info.value)

    def test_decrease_stock_negative_quantity(self):
        """Test that negative quantity raises error."""
        product = Product.objects.create(
            barcode="STOCK003",
            name="Negative Test",
            price=Decimal("10.00"),
            stock=10,
        )

        with pytest.raises(ValidationError) as exc_info:
            product.decrease_stock(-5)

        assert "Quantity must be positive" in str(exc_info.value)

    def test_increase_stock(self):
        """Test increasing product stock."""
        product = Product.objects.create(
            barcode="STOCK004",
            name="Increase Test",
            price=Decimal("10.00"),
            stock=5,
        )

        product.increase_stock(10)
        assert product.stock == 15

    def test_increase_stock_negative_quantity(self):
        """Test that negative quantity raises error."""
        product = Product.objects.create(
            barcode="STOCK005",
            name="Negative Increase",
            price=Decimal("10.00"),
            stock=5,
        )

        with pytest.raises(ValidationError) as exc_info:
            product.increase_stock(-3)

        assert "Quantity must be positive" in str(exc_info.value)

    def test_default_values(self):
        """Test model default values."""
        product = Product.objects.create(
            barcode="DEFAULT001",
            name="Default Test",
            price=Decimal("10.00"),
        )

        assert product.cost == Decimal("0.00")
        assert product.stock == 0
        assert product.category == ""
        assert product.is_active is True

    def test_name_normalization(self):
        """Test that product name is trimmed."""
        product = Product.objects.create(
            barcode="TRIM001",
            name="  Trimmed Name  ",
            price=Decimal("10.00"),
        )

        assert product.name == "Trimmed Name"

    def test_ordering(self):
        """Test that products are ordered by name."""
        Product.objects.create(
            barcode="Z001", name="Zebra Product", price=Decimal("10.00")
        )
        Product.objects.create(
            barcode="A001", name="Apple Product", price=Decimal("10.00")
        )
        Product.objects.create(
            barcode="M001", name="Mango Product", price=Decimal("10.00")
        )

        products = list(Product.objects.all())
        assert products[0].name == "Apple Product"
        assert products[1].name == "Mango Product"
        assert products[2].name == "Zebra Product"

