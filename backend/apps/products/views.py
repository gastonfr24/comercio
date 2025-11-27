"""
Views for products app.
"""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from .models import Product
from .serializers import ProductSerializer, ProductListSerializer


class ProductPagination(PageNumberPagination):
    """
    Pagination class for products.
    """

    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 100


class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing products.

    Provides CRUD operations for products with filtering and search.

    Endpoints:
        GET /api/products/ - List all products
        POST /api/products/ - Create new product
        GET /api/products/{id}/ - Retrieve product details
        PUT /api/products/{id}/ - Update product
        PATCH /api/products/{id}/ - Partial update product
        DELETE /api/products/{id}/ - Delete product

    Filters:
        - is_active: Filter by active status
        - category: Filter by category
        - price: Filter by price (exact, gte, lte)
        - stock: Filter by stock (exact, gte, lte)

    Search:
        - Search by name, barcode, or category

    Ordering:
        - Order by name, price, stock, created_at
    """

    queryset = Product.objects.all()
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        "is_active": ["exact"],
        "category": ["exact", "icontains"],
        "price": ["exact", "gte", "lte"],
        "stock": ["exact", "gte", "lte"],
    }
    search_fields = ["name", "barcode", "category"]
    ordering_fields = ["name", "price", "stock", "created_at"]
    ordering = ["name"]

    def get_serializer_class(self):
        """
        Get appropriate serializer based on action.

        Returns:
            ProductListSerializer for list action,
            ProductSerializer for other actions
        """
        if self.action == "list":
            return ProductListSerializer
        return ProductSerializer

    @action(detail=False, methods=["get"])
    def low_stock(self, request):
        """
        Get products with low stock (less than 10 units).

        Returns:
            200 OK: List of products with low stock
        """
        threshold = int(request.query_params.get("threshold", 10))
        products = Product.objects.filter(stock__lt=threshold, is_active=True)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def out_of_stock(self, request):
        """
        Get products that are out of stock.

        Returns:
            200 OK: List of out of stock products
        """
        products = Product.objects.filter(stock=0, is_active=True)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

