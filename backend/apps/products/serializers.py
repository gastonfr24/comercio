"""
Serializers for products app.
"""

from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model.

    Includes all product fields and calculated profit_margin.
    """

    profit_margin = serializers.ReadOnlyField()
    in_stock = serializers.ReadOnlyField()

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
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate(self, data):
        """
        Validate that price is not lower than cost.
        """
        price = data.get("price")
        cost = data.get("cost")

        # Si ambos están presentes, validar
        if price is not None and cost is not None:
            if price < cost:
                raise serializers.ValidationError(
                    {"price": "Price cannot be lower than cost."}
                )

        # Si solo price está presente (update), validar contra cost existente
        if price is not None and cost is None and self.instance:
            if price < self.instance.cost:
                raise serializers.ValidationError(
                    {"price": "Price cannot be lower than cost."}
                )

        # Si solo cost está presente (update), validar contra price existente
        if cost is not None and price is None and self.instance:
            if self.instance.price < cost:
                raise serializers.ValidationError(
                    {"cost": "Cost cannot be higher than price."}
                )

        return data


class ProductListSerializer(serializers.ModelSerializer):
    """
    Lightweight serializer for listing products.

    Only includes essential fields for better performance.
    """

    profit_margin = serializers.ReadOnlyField()
    in_stock = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = [
            "id",
            "barcode",
            "name",
            "price",
            "stock",
            "category",
            "profit_margin",
            "in_stock",
        ]
