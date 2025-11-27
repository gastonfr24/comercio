"""
API tests for sales app.
"""
from decimal import Decimal
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.products.models import Product
from .models import Sale, SaleItem


class SaleAPITestCase(APITestCase):
    """Test case for Sale API endpoints."""

    def setUp(self):
        """Set up test data."""
        # Create test products
        self.product1 = Product.objects.create(
            barcode="TEST001",
            name="Test Product 1",
            price=Decimal("10.00"),
            cost=Decimal("5.00"),
            stock=100,
        )

        self.product2 = Product.objects.create(
            barcode="TEST002",
            name="Test Product 2",
            price=Decimal("20.00"),
            cost=Decimal("10.00"),
            stock=50,
        )

        self.inactive_product = Product.objects.create(
            barcode="TEST003",
            name="Inactive Product",
            price=Decimal("15.00"),
            cost=Decimal("7.50"),
            stock=10,
            is_active=False,
        )

    def test_create_sale_success(self):
        """Test successful sale creation."""
        url = reverse("sale-list")
        data = {
            "payment_method": "cash",
            "items": [
                {"product_id": self.product1.id, "quantity": 2},
                {"product_id": self.product2.id, "quantity": 1},
            ],
        }

        response = self.api_client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sale.objects.count(), 1)

        sale = Sale.objects.first()
        self.assertEqual(sale.status, "completed")
        self.assertEqual(sale.payment_type, "cash")
        self.assertEqual(sale.total, Decimal("40.00"))  # (10*2) + (20*1)
        self.assertEqual(sale.items.count(), 2)

        # Verify stock was deducted
        self.product1.refresh_from_db()
        self.product2.refresh_from_db()
        self.assertEqual(self.product1.stock, 98)  # 100 - 2
        self.assertEqual(self.product2.stock, 49)  # 50 - 1

    def test_create_sale_empty_items(self):
        """Test sale creation fails with empty items list."""
        url = reverse("sale-list")
        data = {"payment_method": "cash", "items": []}

        response = self.api_client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("items", response.data)

    def test_create_sale_insufficient_stock(self):
        """Test sale creation fails with insufficient stock."""
        url = reverse("sale-list")
        data = {
            "payment_method": "cash",
            "items": [{"product_id": self.product1.id, "quantity": 150}],
        }

        response = self.api_client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Insufficient stock", str(response.data))

        # Verify stock was not modified
        self.product1.refresh_from_db()
        self.assertEqual(self.product1.stock, 100)

    def test_create_sale_inactive_product(self):
        """Test sale creation fails with inactive product."""
        url = reverse("sale-list")
        data = {
            "payment_method": "cash",
            "items": [{"product_id": self.inactive_product.id, "quantity": 1}],
        }

        response = self.api_client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("not available", str(response.data))

    def test_create_sale_nonexistent_product(self):
        """Test sale creation fails with non-existent product."""
        url = reverse("sale-list")
        data = {
            "payment_method": "cash",
            "items": [{"product_id": 9999, "quantity": 1}],
        }

        response = self.api_client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_sale_invalid_quantity(self):
        """Test sale creation fails with invalid quantity."""
        url = reverse("sale-list")
        data = {
            "payment_method": "cash",
            "items": [{"product_id": self.product1.id, "quantity": 0}],
        }

        response = self.api_client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("items", response.data)
        # Check that there's an error related to quantity
        self.assertTrue(
            "quantity" in str(response.data).lower() or "min_value" in str(response.data)
        )

    def test_create_sale_invalid_payment_method(self):
        """Test sale creation fails with invalid payment method."""
        url = reverse("sale-list")
        data = {
            "payment_method": "crypto",
            "items": [{"product_id": self.product1.id, "quantity": 1}],
        }

        response = self.api_client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Invalid payment method", str(response.data))

    def test_list_sales(self):
        """Test listing sales."""
        # Create test sales
        Sale.objects.create(
            payment_type="cash", total=Decimal("50.00"), status="completed"
        )
        Sale.objects.create(
            payment_type="card", total=Decimal("100.00"), status="completed"
        )

        url = reverse("sale-list")
        response = self.api_client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)

    def test_retrieve_sale(self):
        """Test retrieving a specific sale."""
        sale = Sale.objects.create(
            payment_type="cash", total=Decimal("50.00"), status="completed"
        )
        SaleItem.objects.create(
            sale=sale, product=self.product1, quantity=2, unit_price=Decimal("10.00")
        )

        url = reverse("sale-detail", args=[sale.id])
        response = self.api_client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], sale.id)
        self.assertEqual(len(response.data["items"]), 1)

    def test_filter_sales_by_status(self):
        """Test filtering sales by status."""
        Sale.objects.create(
            payment_type="cash", total=Decimal("50.00"), status="completed"
        )
        Sale.objects.create(
            payment_type="cash", total=Decimal("30.00"), status="cancelled"
        )

        url = reverse("sale-list")
        response = self.api_client.get(url, {"status": "completed"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["status"], "completed")

    def test_filter_sales_by_payment_method(self):
        """Test filtering sales by payment method."""
        Sale.objects.create(
            payment_type="cash", total=Decimal("50.00"), status="completed"
        )
        Sale.objects.create(
            payment_type="card", total=Decimal("100.00"), status="completed"
        )

        url = reverse("sale-list")
        response = self.api_client.get(url, {"payment_type": "card"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["payment_method"], "card")

    def test_cancel_sale(self):
        """Test cancelling a completed sale."""
        # Create a completed sale
        sale = Sale.objects.create(
            payment_type="cash", total=Decimal("20.00"), status="pending"
        )
        SaleItem.objects.create(
            sale=sale,
            product=self.product1,
            quantity=5,
            unit_price=self.product1.price,
        )
        sale.complete_sale()

        # Verify stock was deducted
        self.product1.refresh_from_db()
        initial_stock = self.product1.stock
        self.assertEqual(initial_stock, 95)  # 100 - 5

        # Cancel the sale
        url = reverse("sale-cancel", args=[sale.id])
        response = self.api_client.post(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify sale status changed
        sale.refresh_from_db()
        self.assertEqual(sale.status, "cancelled")

        # Verify stock was restored
        self.product1.refresh_from_db()
        self.assertEqual(self.product1.stock, 100)  # Back to original

    def test_cancel_non_completed_sale_fails(self):
        """Test cancelling a non-completed sale fails."""
        sale = Sale.objects.create(
            payment_type="cash", total=Decimal("20.00"), status="pending"
        )

        url = reverse("sale-cancel", args=[sale.id])
        response = self.api_client.post(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Only completed sales", str(response.data))

    def test_sale_profit_calculation(self):
        """Test sale profit calculation."""
        url = reverse("sale-list")
        data = {
            "payment_method": "cash",
            "items": [
                {"product_id": self.product1.id, "quantity": 2},  # profit: $5 each
                {"product_id": self.product2.id, "quantity": 1},  # profit: $10
            ],
        }

        response = self.api_client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data["total_profit"], Decimal("20.00")
        )  # (5*2) + 10

    @property
    def api_client(self):
        """Get API client."""
        return self.client

