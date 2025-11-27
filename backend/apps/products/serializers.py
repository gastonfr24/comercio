"""
Serializers for products app.
"""
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model (full details).

    Provides complete product information including calculated properties.
    """

    profit_margin = serializers.DecimalField(
        max_digits=5, decimal_places=2, read_only=True
    )
    in_stock = serializers.BooleanField(read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "barcode",
            "name",
            "price",
            "cost",
            "stock",
            "category",
            "is_active",
            "profit_margin",
            "in_stock",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "profit_margin", "in_stock"]

    def validate_barcode(self, value):
        """
        Validate that barcode is unique.

        Args:
            value: Barcode to validate

        Returns:
            Barcode if valid

        Raises:
            ValidationError: If barcode already exists
        """
        instance = self.instance
        if instance and instance.barcode == value:
            return value

        if Product.objects.filter(barcode=value).exists():
            raise serializers.ValidationError(
                f"Product with barcode '{value}' already exists."
            )

        return value

    def validate_price(self, value):
        """
        Validate that price is positive.

        Args:
            value: Price to validate

        Returns:
            Price if valid

        Raises:
            ValidationError: If price is not positive
        """
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")

        return value

    def validate_cost(self, value):
        """
        Validate that cost is positive.

        Args:
            value: Cost to validate

        Returns:
            Cost if valid

        Raises:
            ValidationError: If cost is not positive
        """
        if value <= 0:
            raise serializers.ValidationError("Cost must be greater than 0.")

        return value

    def validate_stock(self, value):
        """
        Validate that stock is non-negative.

        Args:
            value: Stock to validate

        Returns:
            Stock if valid

        Raises:
            ValidationError: If stock is negative
        """
        if value < 0:
            raise serializers.ValidationError("Stock cannot be negative.")

        return value


class ProductListSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model (list view).

    Provides minimal product information for list views.
    """

    in_stock = serializers.BooleanField(read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "barcode",
            "name",
            "price",
            "stock",
            "category",
            "is_active",
            "in_stock",
        ]
        read_only_fields = fields

