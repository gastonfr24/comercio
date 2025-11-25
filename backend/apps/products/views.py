"""
Views for products app.
"""

from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer, ProductListSerializer


class ProductPagination(PageNumberPagination):
    """
    Custom pagination for products.
    """

    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 100


class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Product model.

    Provides CRUD operations for products with filtering and search capabilities.

    Filters:
        - search: Search by name or barcode
        - category: Filter by category
        - is_active: Filter by active status

    Ordering:
        - Default: name (ascending)
        - Available: name, price, stock, created_at
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Filtros exactos
    filterset_fields = ["category", "is_active"]

    # Búsqueda por nombre y barcode
    search_fields = ["name", "barcode"]

    # Ordenamiento disponible
    ordering_fields = ["name", "price", "stock", "created_at"]
    ordering = ["name"]

    def get_serializer_class(self):
        """
        Use lightweight serializer for list action.
        """
        if self.action == "list":
            return ProductListSerializer
        return ProductSerializer

    def get_queryset(self):
        """
        Filter queryset to only show active products by default.

        Use ?is_active=false to include inactive products.
        """
        queryset = super().get_queryset()

        # Por defecto, solo mostrar productos activos
        if self.action == "list":
            is_active = self.request.query_params.get("is_active", None)
            if is_active is None:
                queryset = queryset.filter(is_active=True)

        return queryset
