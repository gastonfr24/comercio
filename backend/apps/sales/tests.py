"""
Tests for sales app.
"""
from decimal import Decimal
import pytest
from django.core.exceptions import ValidationError
from apps.products.models import Product
from .models import Sale, SaleItem


@pytest.fixture
def sample_product(db):
    """
    Fixture to create a sample product.
    """
    return Product.objects.create(
        barcode="123456789",
        name="Test Product",
        price=Decimal("10.00"),
        cost=Decimal("5.00"),
        stock=100,
    )


@pytest.fixture
def sample_sale(db):
    """
    Fixture to create a sample sale.
    """
    return Sale.objects.create(
        total=Decimal("50.00"), payment_type="cash", status="pending"
    )


@pytest.fixture
def sample_sale_with_items(db, sample_product):
    """
    Fixture to create a sale with items.
    """
    sale = Sale.objects.create(
        total=Decimal("30.00"), payment_type="cash", status="pending"
    )

    SaleItem.objects.create(
        sale=sale,
        product=sample_product,
        quantity=3,
        unit_price=sample_product.price,
        subtotal=Decimal("30.00"),
    )

    return sale


@pytest.mark.django_db
class TestSaleModel:
    """
    Tests for Sale model.
    """

    def test_create_sale(self):
        """
        Test creating a sale.
        """
        sale = Sale.objects.create(
            total=Decimal("100.50"), payment_type="card", status="pending"
        )

        assert sale.id is not None
        assert sale.total == Decimal("100.50")
        assert sale.payment_type == "card"
        assert sale.status == "pending"
        assert sale.date is not None

    def test_sale_str_representation(self):
        """
        Test string representation of Sale.
        """
        sale = Sale.objects.create(total=Decimal("50.00"))
        assert str(sale) == f"Sale #{sale.id} - $50.00"

    def test_sale_default_values(self):
        """
        Test default values of Sale.
        """
        sale = Sale.objects.create(total=Decimal("10.00"))

        assert sale.payment_type == "cash"
        assert sale.status == "pending"

    def test_sale_payment_types(self):
        """
        Test different payment types.
        """
        sale_cash = Sale.objects.create(
            total=Decimal("10.00"), payment_type="cash"
        )
        sale_card = Sale.objects.create(
            total=Decimal("20.00"), payment_type="card"
        )
        sale_transfer = Sale.objects.create(
            total=Decimal("30.00"), payment_type="transfer"
        )

        assert sale_cash.payment_type == "cash"
        assert sale_card.payment_type == "card"
        assert sale_transfer.payment_type == "transfer"

    def test_sale_invalid_total(self):
        """
        Test creating sale with invalid total.
        """
        with pytest.raises(ValidationError) as exc_info:
            sale = Sale(total=Decimal("-10.00"))
            sale.save()

        assert "total" in str(exc_info.value)

    def test_sale_zero_total(self):
        """
        Test creating sale with zero total.
        """
        with pytest.raises(ValidationError) as exc_info:
            sale = Sale(total=Decimal("0.00"))
            sale.save()

        assert "total" in str(exc_info.value)

    def test_calculate_total(self, sample_sale_with_items):
        """
        Test calculating total from sale items.
        """
        calculated_total = sample_sale_with_items.calculate_total()
        assert calculated_total == Decimal("30.00")

    def test_complete_sale(self, sample_sale_with_items, sample_product):
        """
        Test completing a sale updates product stock.
        """
        initial_stock = sample_product.stock

        sample_sale_with_items.complete_sale()

        sample_product.refresh_from_db()
        assert sample_sale_with_items.status == "completed"
        assert sample_product.stock == initial_stock - 3

    def test_complete_sale_already_completed(self, sample_sale_with_items):
        """
        Test completing an already completed sale raises error.
        """
        sample_sale_with_items.complete_sale()

        with pytest.raises(ValidationError) as exc_info:
            sample_sale_with_items.complete_sale()

        assert "Cannot complete sale" in str(exc_info.value)

    def test_cancel_pending_sale(self, sample_sale):
        """
        Test cancelling a pending sale.
        """
        sample_sale.cancel_sale()

        assert sample_sale.status == "cancelled"

    def test_cancel_completed_sale_restores_stock(
        self, sample_sale_with_items, sample_product
    ):
        """
        Test cancelling a completed sale restores stock.
        """
        # Completar la venta primero
        sample_sale_with_items.complete_sale()
        sample_product.refresh_from_db()
        stock_after_complete = sample_product.stock

        # Cancelar la venta
        sample_sale_with_items.cancel_sale()
        sample_product.refresh_from_db()

        assert sample_sale_with_items.status == "cancelled"
        assert sample_product.stock == stock_after_complete + 3

    def test_cancel_already_cancelled_sale(self, sample_sale):
        """
        Test cancelling an already cancelled sale raises error.
        """
        sample_sale.cancel_sale()

        with pytest.raises(ValidationError) as exc_info:
            sample_sale.cancel_sale()

        assert "already cancelled" in str(exc_info.value)

    def test_sale_ordering(self, db):
        """
        Test sales are ordered by date (newest first).
        """
        sale1 = Sale.objects.create(total=Decimal("10.00"))
        sale2 = Sale.objects.create(total=Decimal("20.00"))
        sale3 = Sale.objects.create(total=Decimal("30.00"))

        sales = list(Sale.objects.all())

        assert sales[0].id == sale3.id
        assert sales[1].id == sale2.id
        assert sales[2].id == sale1.id


@pytest.mark.django_db
class TestSaleItemModel:
    """
    Tests for SaleItem model.
    """

    def test_create_sale_item(self, sample_sale, sample_product):
        """
        Test creating a sale item.
        """
        item = SaleItem.objects.create(
            sale=sample_sale,
            product=sample_product,
            quantity=2,
            unit_price=sample_product.price,
            subtotal=Decimal("20.00"),
        )

        assert item.id is not None
        assert item.sale == sample_sale
        assert item.product == sample_product
        assert item.quantity == 2
        assert item.unit_price == sample_product.price
        assert item.subtotal == Decimal("20.00")

    def test_sale_item_str_representation(self, sample_sale, sample_product):
        """
        Test string representation of SaleItem.
        """
        item = SaleItem.objects.create(
            sale=sample_sale,
            product=sample_product,
            quantity=5,
            unit_price=sample_product.price,
        )

        assert str(item) == f"5x {sample_product.name}"

    def test_calculate_subtotal(self, sample_sale, sample_product):
        """
        Test calculating subtotal.
        """
        item = SaleItem(
            sale=sample_sale,
            product=sample_product,
            quantity=3,
            unit_price=Decimal("10.00"),
        )

        subtotal = item.calculate_subtotal()
        assert subtotal == Decimal("30.00")

    def test_auto_calculate_subtotal_on_save(self, sample_sale, sample_product):
        """
        Test subtotal is calculated automatically on save.
        """
        item = SaleItem.objects.create(
            sale=sample_sale,
            product=sample_product,
            quantity=4,
            unit_price=Decimal("12.50"),
        )

        assert item.subtotal == Decimal("50.00")

    def test_sale_item_invalid_quantity(self, sample_sale, sample_product):
        """
        Test creating sale item with zero quantity.
        """
        with pytest.raises(ValidationError):
            item = SaleItem(
                sale=sample_sale,
                product=sample_product,
                quantity=0,
                unit_price=Decimal("10.00"),
            )
            item.save()

    def test_sale_item_negative_quantity(self, sample_sale, sample_product):
        """
        Test creating sale item with negative quantity raises validation error.
        """
        with pytest.raises((ValidationError, ValueError)):
            item = SaleItem(
                sale=sample_sale,
                product=sample_product,
                quantity=-1,
                unit_price=Decimal("10.00"),
            )
            item.save()

    def test_sale_item_invalid_unit_price(self, sample_sale, sample_product):
        """
        Test creating sale item with zero unit price.
        """
        with pytest.raises(ValidationError):
            item = SaleItem(
                sale=sample_sale,
                product=sample_product,
                quantity=1,
                unit_price=Decimal("0.00"),
            )
            item.save()

    def test_sale_item_inactive_product(self, sample_sale, sample_product):
        """
        Test creating sale item with inactive product raises error.
        """
        sample_product.is_active = False
        sample_product.save()

        with pytest.raises(ValidationError) as exc_info:
            item = SaleItem(
                sale=sample_sale,
                product=sample_product,
                quantity=1,
                unit_price=Decimal("10.00"),
            )
            item.save()

        assert "not active" in str(exc_info.value)

    def test_sale_item_insufficient_stock(self, sample_sale, sample_product):
        """
        Test creating sale item with insufficient stock raises error.
        """
        sample_product.stock = 2
        sample_product.save()

        with pytest.raises(ValidationError) as exc_info:
            item = SaleItem(
                sale=sample_sale,
                product=sample_product,
                quantity=10,
                unit_price=Decimal("10.00"),
            )
            item.save()

        assert "Insufficient stock" in str(exc_info.value)

    def test_sale_item_out_of_stock(self, sample_sale, sample_product):
        """
        Test creating sale item with out of stock product raises error.
        """
        sample_product.stock = 0
        sample_product.save()

        with pytest.raises(ValidationError) as exc_info:
            item = SaleItem(
                sale=sample_sale,
                product=sample_product,
                quantity=1,
                unit_price=Decimal("10.00"),
            )
            item.save()

        assert "Insufficient stock" in str(exc_info.value)

    def test_multiple_items_in_sale(self, sample_sale, db):
        """
        Test adding multiple items to a sale.
        """
        product1 = Product.objects.create(
            barcode="111",
            name="Product 1",
            price=Decimal("10.00"),
            cost=Decimal("5.00"),
            stock=10,
        )
        product2 = Product.objects.create(
            barcode="222",
            name="Product 2",
            price=Decimal("15.00"),
            cost=Decimal("8.00"),
            stock=10,
        )

        SaleItem.objects.create(
            sale=sample_sale,
            product=product1,
            quantity=2,
            unit_price=product1.price,
        )
        SaleItem.objects.create(
            sale=sample_sale,
            product=product2,
            quantity=3,
            unit_price=product2.price,
        )

        assert sample_sale.items.count() == 2
        total = sample_sale.calculate_total()
        assert total == Decimal("65.00")  # (2*10) + (3*15)

