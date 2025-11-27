"""
API tests for products app.
"""

from decimal import Decimal
import pytest
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product


@pytest.fixture
def api_client():
    """
    Fixture to provide API client.
    """
    return APIClient()


@pytest.fixture
def sample_products(db):
    """
    Fixture to create sample products for testing.
    """
    products = [
        Product.objects.create(
            barcode="123456789",
            name="Coca Cola 500ml",
            price=Decimal("2.50"),
            cost=Decimal("1.50"),
            stock=50,
            category="Bebidas",
        ),
        Product.objects.create(
            barcode="987654321",
            name="Pepsi 500ml",
            price=Decimal("2.30"),
            cost=Decimal("1.40"),
            stock=30,
            category="Bebidas",
        ),
        Product.objects.create(
            barcode="111222333",
            name="Alfajor Jorgito",
            price=Decimal("1.20"),
            cost=Decimal("0.70"),
            stock=100,
            category="Golosinas",
        ),
        Product.objects.create(
            barcode="444555666",
            name="Papas Lays",
            price=Decimal("3.00"),
            cost=Decimal("2.00"),
            stock=0,
            category="Snacks",
        ),
        Product.objects.create(
            barcode="777888999",
            name="Producto Inactivo",
            price=Decimal("5.00"),
            cost=Decimal("3.00"),
            stock=10,
            category="Otros",
            is_active=False,
        ),
    ]
    return products


@pytest.mark.django_db
class TestProductListAPI:
    """
    Tests for GET /api/products/ endpoint.
    """

    def test_list_products(self, api_client, sample_products):
        """
        Test listing all active products.
        """
        response = api_client.get("/api/products/")

        assert response.status_code == status.HTTP_200_OK
        assert "results" in response.data
        assert "count" in response.data

        # Solo productos activos (4 de 5)
        assert response.data["count"] == 4

        # Verificar campos del serializer ligero
        first_product = response.data["results"][0]
        assert "id" in first_product
        assert "barcode" in first_product
        assert "name" in first_product
        assert "price" in first_product
        assert "stock" in first_product
        assert "category" in first_product
        assert "profit_margin" in first_product
        assert "in_stock" in first_product

        # No debe incluir campos del serializer completo
        assert "cost" not in first_product

    def test_list_includes_inactive_when_requested(self, api_client, sample_products):
        """
        Test listing products including inactive ones.
        """
        response = api_client.get("/api/products/?is_active=false")

        assert response.status_code == status.HTTP_200_OK
        # Debe incluir el producto inactivo
        names = [p["name"] for p in response.data["results"]]
        assert "Producto Inactivo" in names

    def test_filter_by_category(self, api_client, sample_products):
        """
        Test filtering products by category.
        """
        response = api_client.get("/api/products/?category=Bebidas")

        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 2

        categories = {p["category"] for p in response.data["results"]}
        assert categories == {"Bebidas"}

    def test_search_by_name(self, api_client, sample_products):
        """
        Test searching products by name.
        """
        response = api_client.get("/api/products/?search=cola")

        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1
        assert "Coca Cola" in response.data["results"][0]["name"]

    def test_search_by_barcode(self, api_client, sample_products):
        """
        Test searching products by barcode.
        """
        response = api_client.get("/api/products/?search=123456")

        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1
        assert response.data["results"][0]["barcode"] == "123456789"

    def test_ordering_by_name(self, api_client, sample_products):
        """
        Test ordering products by name.
        """
        response = api_client.get("/api/products/")

        assert response.status_code == status.HTTP_200_OK
        names = [p["name"] for p in response.data["results"]]

        # Default ordering is by name
        assert names == sorted(names)

    def test_ordering_by_price(self, api_client, sample_products):
        """
        Test ordering products by price.
        """
        response = api_client.get("/api/products/?ordering=price")

        assert response.status_code == status.HTTP_200_OK
        prices = [Decimal(str(p["price"])) for p in response.data["results"]]

        assert prices == sorted(prices)

    def test_pagination(self, api_client, db):
        """
        Test pagination of products.
        """
        # Crear 25 productos
        for i in range(25):
            Product.objects.create(
                barcode=f"BAR{i:05d}",
                name=f"Product {i}",
                price=Decimal("10.00"),
                cost=Decimal("5.00"),
                stock=10,
            )

        # Primera página (default: 20 items)
        response = api_client.get("/api/products/")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 20
        assert response.data["count"] == 25

        # Segunda página
        response = api_client.get("/api/products/?page=2")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 5

    def test_custom_page_size(self, api_client, sample_products):
        """
        Test custom page size.
        """
        response = api_client.get("/api/products/?page_size=2")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 2


@pytest.mark.django_db
class TestProductDetailAPI:
    """
    Tests for GET /api/products/{id}/ endpoint.
    """

    def test_get_product_detail(self, api_client, sample_products):
        """
        Test getting product detail.
        """
        product = sample_products[0]
        response = api_client.get(f"/api/products/{product.id}/")

        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == product.id
        assert response.data["barcode"] == product.barcode
        assert response.data["name"] == product.name

        # Debe incluir todos los campos del serializer completo
        assert "cost" in response.data
        assert "profit_margin" in response.data
        assert "created_at" in response.data
        assert "updated_at" in response.data

    def test_get_nonexistent_product(self, api_client):
        """
        Test getting a product that doesn't exist.
        """
        response = api_client.get("/api/products/99999/")

        assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
class TestProductCreateAPI:
    """
    Tests for POST /api/products/ endpoint.
    """

    def test_create_product(self, api_client):
        """
        Test creating a new product.
        """
        data = {
            "barcode": "555666777",
            "name": "New Product",
            "price": "10.00",
            "cost": "6.00",
            "stock": 20,
            "category": "Test",
        }

        response = api_client.post("/api/products/", data, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["barcode"] == "555666777"
        assert response.data["name"] == "New Product"

        # Verificar que se creó en la base de datos
        assert Product.objects.filter(barcode="555666777").exists()

    def test_create_product_with_invalid_price(self, api_client):
        """
        Test creating a product with price lower than cost.
        """
        data = {
            "barcode": "555666777",
            "name": "Invalid Product",
            "price": "5.00",
            "cost": "10.00",
            "stock": 20,
        }

        response = api_client.post("/api/products/", data, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "price" in response.data

    def test_create_product_with_duplicate_barcode(self, api_client, sample_products):
        """
        Test creating a product with duplicate barcode.
        """
        data = {
            "barcode": "123456789",  # Ya existe
            "name": "Duplicate Product",
            "price": "10.00",
            "cost": "6.00",
            "stock": 20,
        }

        response = api_client.post("/api/products/", data, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestProductUpdateAPI:
    """
    Tests for PUT/PATCH /api/products/{id}/ endpoint.
    """

    def test_update_product(self, api_client, sample_products):
        """
        Test updating a product.
        """
        product = sample_products[0]
        data = {
            "name": "Updated Name",
            "price": "3.00",
        }

        response = api_client.patch(f"/api/products/{product.id}/", data, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == "Updated Name"
        assert Decimal(response.data["price"]) == Decimal("3.00")

        # Verificar en la base de datos
        product.refresh_from_db()
        assert product.name == "Updated Name"

    def test_update_product_invalid_price(self, api_client, sample_products):
        """
        Test updating product with invalid price (lower than cost).
        """
        product = sample_products[0]
        data = {
            "price": "1.00",  # cost es 1.50
        }

        response = api_client.patch(f"/api/products/{product.id}/", data, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestProductDeleteAPI:
    """
    Tests for DELETE /api/products/{id}/ endpoint.
    """

    def test_delete_product(self, api_client, sample_products):
        """
        Test deleting a product.
        """
        product = sample_products[0]
        product_id = product.id

        response = api_client.delete(f"/api/products/{product_id}/")

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Product.objects.filter(id=product_id).exists()


@pytest.mark.django_db
class TestProductSearchAPI:
    """
    Tests for GET /api/products/search/ endpoint.
    """

    def test_search_by_exact_barcode(self, api_client, sample_products):
        """
        Test searching by exact barcode match.
        """
        response = api_client.get("/api/products/search/?q=123456789")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["barcode"] == "123456789"
        assert response.data[0]["name"] == "Coca Cola 500ml"

    def test_search_by_barcode_case_insensitive(self, api_client, sample_products):
        """
        Test searching by barcode is case-insensitive.
        """
        # Create a product with alphanumeric barcode
        Product.objects.create(
            barcode="ABC123",
            name="Test Product",
            price=Decimal("5.00"),
            cost=Decimal("3.00"),
            stock=10,
        )

        response = api_client.get("/api/products/search/?q=abc123")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["barcode"] == "ABC123"

    def test_search_by_name(self, api_client, sample_products):
        """
        Test searching by product name (partial match).
        """
        response = api_client.get("/api/products/search/?q=coca")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert "Coca" in response.data[0]["name"]

    def test_search_by_name_case_insensitive(self, api_client, sample_products):
        """
        Test searching by name is case-insensitive.
        """
        response = api_client.get("/api/products/search/?q=PEPSI")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert "Pepsi" in response.data[0]["name"]

    def test_search_multiple_results(self, api_client, sample_products):
        """
        Test searching returns multiple results when applicable.
        """
        response = api_client.get("/api/products/search/?q=500ml")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2  # Coca Cola and Pepsi

    def test_search_no_results(self, api_client, sample_products):
        """
        Test searching with no matches returns empty list.
        """
        response = api_client.get("/api/products/search/?q=nonexistent")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 0

    def test_search_only_active_products(self, api_client, sample_products):
        """
        Test searching only returns active products.
        """
        # Deactivate Coca Cola
        product = Product.objects.get(barcode="123456789")
        product.is_active = False
        product.save()

        response = api_client.get("/api/products/search/?q=coca")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 0

    def test_search_missing_query_parameter(self, api_client):
        """
        Test searching without query parameter returns 400.
        """
        response = api_client.get("/api/products/search/")

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "error" in response.data

    def test_search_empty_query_parameter(self, api_client):
        """
        Test searching with empty query parameter returns 400.
        """
        response = api_client.get("/api/products/search/?q=")

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "error" in response.data

    def test_search_limits_results(self, api_client):
        """
        Test searching limits results to 10 items.
        """
        # Create 15 products with similar names
        for i in range(15):
            Product.objects.create(
                barcode=f"TEST{i:03d}",
                name=f"Test Product {i}",
                price=Decimal("1.00"),
                cost=Decimal("0.50"),
                stock=10,
            )

        response = api_client.get("/api/products/search/?q=Test Product")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) <= 10

    def test_search_barcode_priority(self, api_client):
        """
        Test that barcode match has priority over name match.
        """
        # Create two products: one with barcode "123", another with "123" in name
        Product.objects.create(
            barcode="123",
            name="Product A",
            price=Decimal("1.00"),
            cost=Decimal("0.50"),
            stock=10,
        )
        Product.objects.create(
            barcode="456",
            name="Product 123 Name",
            price=Decimal("2.00"),
            cost=Decimal("1.00"),
            stock=10,
        )

        response = api_client.get("/api/products/search/?q=123")

        assert response.status_code == status.HTTP_200_OK
        # Should only return the barcode match
        assert len(response.data) == 1
        assert response.data[0]["barcode"] == "123"
