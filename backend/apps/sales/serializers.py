"""
Serializers for sales app.
"""

from decimal import Decimal
from rest_framework import serializers
from django.db import transaction
from .models import Sale, SaleItem
from apps.products.models import Product


class SaleItemSerializer(serializers.ModelSerializer):
    """
    Serializer for SaleItem model.

    Provides product details in read operations and accepts
    product_id for write operations.
    """

    product_id = serializers.IntegerField(write_only=True)
    product_name = serializers.CharField(source="product.name", read_only=True)
    product_barcode = serializers.CharField(source="product.barcode", read_only=True)
    unit_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = SaleItem
        fields = [
            "id",
            "product_id",
            "product_name",
            "product_barcode",
            "quantity",
            "unit_price",
            "subtotal",
        ]
        read_only_fields = ["id", "unit_price", "subtotal"]

    def validate_product_id(self, value):
        """
        Validate that product exists and is active.

        Args:
            value: Product ID to validate

        Returns:
            Product ID if valid

        Raises:
            ValidationError: If product doesn't exist or is inactive
        """
        try:
            product = Product.objects.get(id=value)
        except Product.DoesNotExist:
            raise serializers.ValidationError(
                f"Product with id {value} does not exist."
            )

        if not product.is_active:
            raise serializers.ValidationError(
                f"Product '{product.name}' is not available for sale."
            )

        return value

    def validate_quantity(self, value):
        """
        Validate that quantity is positive.

        Args:
            value: Quantity to validate

        Returns:
            Quantity if valid

        Raises:
            ValidationError: If quantity is not positive
        """
        if value <= 0:
            raise serializers.ValidationError("Quantity must be greater than 0.")

        return value


class CreateSaleSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a sale with items.

    Handles atomic creation of sale and items with stock validation
    and automatic stock deduction.
    """

    items = SaleItemSerializer(many=True, write_only=True)
    sale_items = SaleItemSerializer(many=True, read_only=True, source="items")
    payment_method = serializers.CharField(source="payment_type", required=False)
    total_amount = serializers.DecimalField(
        source="total", max_digits=10, decimal_places=2, read_only=True
    )
    sale_date = serializers.DateTimeField(source="date", read_only=True)

    class Meta:
        model = Sale
        fields = [
            "id",
            "sale_date",
            "total_amount",
            "payment_method",
            "status",
            "items",
            "sale_items",
            "created_at",
        ]
        read_only_fields = ["id", "sale_date", "total_amount", "created_at"]

    def validate_items(self, value):
        """
        Validate that items list is not empty and stock is available.

        Args:
            value: List of sale items

        Returns:
            List of items if valid

        Raises:
            ValidationError: If items list is empty or stock is insufficient
        """
        if not value:
            raise serializers.ValidationError("Sale must have at least one item.")

        # Check stock availability for each item
        for item_data in value:
            product_id = item_data.get("product_id")
            quantity = item_data.get("quantity")

            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                raise serializers.ValidationError(
                    f"Product with id {product_id} does not exist."
                )

            if product.stock < quantity:
                raise serializers.ValidationError(
                    f"Insufficient stock for '{product.name}'. "
                    f"Available: {product.stock}, Requested: {quantity}"
                )

        return value

    def validate_payment_method(self, value):
        """
        Validate payment method.

        Args:
            value: Payment method to validate

        Returns:
            Payment method if valid

        Raises:
            ValidationError: If payment method is invalid
        """
        valid_methods = ["cash", "card", "transfer"]
        if value not in valid_methods:
            raise serializers.ValidationError(
                f"Invalid payment method. Must be one of: {', '.join(valid_methods)}"
            )

        return value

    @transaction.atomic
    def create(self, validated_data):
        """
        Create sale with items atomically.

        Creates the sale and all items in a single transaction.
        Automatically calculates totals and deducts stock.

        Args:
            validated_data: Validated data from serializer

        Returns:
            Created Sale instance with items
        """
        items_data = validated_data.pop("items")

        # Get payment_type from validated_data (mapped from payment_method)
        payment_type = validated_data.pop("payment_type", "cash")

        # Create sale with pending status and initial total
        sale = Sale.objects.create(
            status="pending",
            payment_type=payment_type,
            total=Decimal("0.01"),  # Temporary value to pass validation
        )

        # Create sale items and calculate total
        total_amount = Decimal("0.00")

        for item_data in items_data:
            product_id = item_data.pop("product_id")
            product = Product.objects.get(id=product_id)

            # Create sale item with product price
            sale_item = SaleItem.objects.create(
                sale=sale,
                product=product,
                quantity=item_data["quantity"],
                unit_price=product.price,
            )

            total_amount += sale_item.subtotal

        # Update sale total
        sale.total = total_amount
        sale.save()

        # Complete the sale (this will deduct stock)
        sale.complete_sale()

        return sale


class SaleSerializer(serializers.ModelSerializer):
    """
    Serializer for Sale model (read operations).

    Provides complete sale information including items.
    """

    items = SaleItemSerializer(many=True, read_only=True)
    payment_method = serializers.CharField(source="payment_type", read_only=True)
    total_amount = serializers.DecimalField(
        source="total", max_digits=10, decimal_places=2, read_only=True
    )
    sale_date = serializers.DateTimeField(source="date", read_only=True)

    # Calculate total profit from items
    total_profit = serializers.SerializerMethodField()

    class Meta:
        model = Sale
        fields = [
            "id",
            "sale_date",
            "total_amount",
            "payment_method",
            "status",
            "items",
            "total_profit",
            "created_at",
            "updated_at",
        ]
        read_only_fields = fields

    def get_total_profit(self, obj):
        """
        Calculate total profit from all sale items.

        Args:
            obj: Sale instance

        Returns:
            Total profit amount
        """
        total_profit = Decimal("0.00")
        for item in obj.items.all():
            profit_per_unit = item.unit_price - item.product.cost
            total_profit += profit_per_unit * item.quantity
        return total_profit.quantize(Decimal("0.01"))
