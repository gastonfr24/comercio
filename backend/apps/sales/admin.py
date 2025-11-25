"""
Admin configuration for sales app.
"""
from django.contrib import admin
from .models import Sale, SaleItem


class SaleItemInline(admin.TabularInline):
    """
    Inline admin for SaleItem within Sale admin.
    """

    model = SaleItem
    extra = 0
    readonly_fields = ["subtotal", "created_at"]
    fields = ["product", "quantity", "unit_price", "subtotal"]
    autocomplete_fields = ["product"]


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    """
    Admin configuration for Sale model.
    """

    list_display = [
        "id",
        "date",
        "total",
        "payment_type",
        "status",
        "items_count",
    ]
    list_filter = ["status", "payment_type", "date"]
    search_fields = ["id"]
    readonly_fields = ["date", "created_at", "updated_at"]
    inlines = [SaleItemInline]
    date_hierarchy = "date"

    fieldsets = (
        (
            "Sale Information",
            {
                "fields": ("total", "payment_type", "status"),
            },
        ),
        (
            "Timestamps",
            {
                "fields": ("date", "created_at", "updated_at"),
                "classes": ("collapse",),
            },
        ),
    )

    def items_count(self, obj):
        """
        Display number of items in the sale.
        """
        return obj.items.count()

    items_count.short_description = "Items"

    def get_queryset(self, request):
        """
        Optimize queryset with prefetch_related.
        """
        queryset = super().get_queryset(request)
        return queryset.prefetch_related("items")


@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    """
    Admin configuration for SaleItem model.
    """

    list_display = [
        "id",
        "sale",
        "product",
        "quantity",
        "unit_price",
        "subtotal",
        "created_at",
    ]
    list_filter = ["created_at"]
    search_fields = ["sale__id", "product__name", "product__barcode"]
    readonly_fields = ["subtotal", "created_at"]
    autocomplete_fields = ["sale", "product"]

    fieldsets = (
        (
            "Item Information",
            {
                "fields": ("sale", "product", "quantity", "unit_price", "subtotal"),
            },
        ),
        (
            "Timestamps",
            {
                "fields": ("created_at",),
                "classes": ("collapse",),
            },
        ),
    )

    def get_queryset(self, request):
        """
        Optimize queryset with select_related.
        """
        queryset = super().get_queryset(request)
        return queryset.select_related("sale", "product")

