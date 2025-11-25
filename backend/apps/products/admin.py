"""
Admin configuration for products app.
"""

from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin interface for Product model."""

    list_display = [
        "barcode",
        "name",
        "category",
        "price",
        "cost",
        "stock",
        "is_active",
        "created_at",
    ]
    list_filter = ["is_active", "category", "created_at"]
    search_fields = ["barcode", "name", "category"]
    readonly_fields = ["created_at", "updated_at", "profit_margin"]
    list_editable = ["is_active", "price", "stock"]
    list_per_page = 50

    fieldsets = [
        (
            "Basic Information",
            {
                "fields": ["barcode", "name", "category", "is_active"],
            },
        ),
        (
            "Pricing",
            {
                "fields": ["cost", "price", "profit_margin"],
            },
        ),
        (
            "Inventory",
            {
                "fields": ["stock"],
            },
        ),
        (
            "Metadata",
            {
                "fields": ["created_at", "updated_at"],
                "classes": ["collapse"],
            },
        ),
    ]

    def profit_margin(self, obj: Product) -> str:
        """
        Display profit margin in admin.

        Args:
            obj: Product instance

        Returns:
            Formatted profit margin percentage
        """
        return f"{obj.profit_margin}%"

    profit_margin.short_description = "Profit Margin"
