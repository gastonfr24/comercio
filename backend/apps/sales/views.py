"""
Views for sales app.
"""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Sale
from .serializers import CreateSaleSerializer, SaleSerializer


class SaleViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing sales.

    Provides CRUD operations for sales with automatic stock management.

    Endpoints:
        GET /api/sales/ - List all sales
        POST /api/sales/ - Create new sale
        GET /api/sales/{id}/ - Retrieve sale details
        POST /api/sales/{id}/cancel/ - Cancel a sale

    Filters:
        - status: Filter by sale status
        - payment_method: Filter by payment method
        - sale_date: Filter by date (exact, gte, lte)

    Search:
        - Search by sale ID or items

    Ordering:
        - Order by sale_date, total_amount, created_at
    """

    queryset = Sale.objects.all().prefetch_related("items__product")
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        "status": ["exact"],
        "payment_type": ["exact"],
        "date": ["exact", "gte", "lte"],
    }
    search_fields = ["id", "items__product__name"]
    ordering_fields = ["date", "total", "created_at"]
    ordering = ["-date"]

    def get_serializer_class(self):
        """
        Get appropriate serializer based on action.

        Returns:
            CreateSaleSerializer for create action,
            SaleSerializer for other actions
        """
        if self.action == "create":
            return CreateSaleSerializer
        return SaleSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a new sale with items.

        Validates stock availability and creates sale atomically.
        Automatically deducts stock upon completion.

        Request Body:
            {
                "payment_method": "cash",
                "items": [
                    {
                        "product_id": 1,
                        "quantity": 2
                    }
                ]
            }

        Returns:
            201 CREATED: Sale created successfully
            400 BAD REQUEST: Validation errors (insufficient stock, etc.)
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        sale = serializer.save()

        # Return sale data with read serializer
        read_serializer = SaleSerializer(sale)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["post"])
    def cancel(self, request, pk=None):
        """
        Cancel a sale and restore stock.

        Only completed sales can be cancelled.

        Returns:
            200 OK: Sale cancelled successfully
            400 BAD REQUEST: Sale cannot be cancelled
            404 NOT FOUND: Sale does not exist
        """
        sale = self.get_object()

        if sale.status != "completed":
            return Response(
                {"error": "Only completed sales can be cancelled."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            sale.cancel_sale()
            serializer = self.get_serializer(sale)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )

