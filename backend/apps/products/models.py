"""
Product models for inventory management.
"""
from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


class Product(models.Model):
    """
    Product model representing items in the inventory.

    This model stores all product information including pricing,
    stock levels, and categorization for the kiosk system.

    Attributes:
        barcode: Unique product barcode for scanner identification
        name: Product display name
        price: Selling price to customers
        cost: Purchase cost from supplier
        stock: Current available quantity
        category: Product category for organization
        is_active: Whether the product is available for sale
        created_at: Timestamp of product creation
        updated_at: Timestamp of last modification
    """

    barcode = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
        help_text="Unique barcode for product identification",
    )
    name = models.CharField(
        max_length=200,
        db_index=True,
        help_text="Product display name",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))],
        help_text="Selling price to customers",
    )
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))],
        default=Decimal("0.00"),
        help_text="Purchase cost from supplier",
    )
    stock = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        help_text="Current available quantity",
    )
    category = models.CharField(
        max_length=100,
        blank=True,
        db_index=True,
        help_text="Product category for organization",
    )
    is_active = models.BooleanField(
        default=True,
        db_index=True,
        help_text="Whether the product is available for sale",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp of product creation",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp of last modification",
    )

    class Meta:
        """Model metadata."""

        ordering = ["name"]
        verbose_name = "Product"
        verbose_name_plural = "Products"
        indexes = [
            models.Index(fields=["barcode"]),
            models.Index(fields=["name"]),
            models.Index(fields=["category", "is_active"]),
        ]

    def __str__(self) -> str:
        """
        String representation of the product.

        Returns:
            Product name and barcode
        """
        return f"{self.name} ({self.barcode})"

    def clean(self) -> None:
        """
        Validate product data.

        Raises:
            ValidationError: If validation fails
        """
        super().clean()

        # Validate that price is greater than or equal to cost
        if self.price < self.cost:
            raise ValidationError({
                "price": "Selling price cannot be lower than cost price."
            })

        # Normalize barcode to uppercase
        if self.barcode:
            self.barcode = self.barcode.strip().upper()

        # Normalize name
        if self.name:
            self.name = self.name.strip()

    def save(self, *args, **kwargs) -> None:
        """
        Save product with validation.

        Args:
            *args: Positional arguments for save method
            **kwargs: Keyword arguments for save method
        """
        self.full_clean()
        super().save(*args, **kwargs)

    @property
    def profit_margin(self) -> Decimal:
        """
        Calculate profit margin percentage.

        Returns:
            Profit margin as a percentage

        Example:
            >>> product.cost = Decimal('50.00')
            >>> product.price = Decimal('75.00')
            >>> product.profit_margin
            Decimal('50.00')
        """
        if self.cost == 0:
            return Decimal("0.00")
        return ((self.price - self.cost) / self.cost * 100).quantize(
            Decimal("0.01")
        )

    @property
    def in_stock(self) -> bool:
        """
        Check if product has stock available.

        Returns:
            True if stock is greater than 0

        Example:
            >>> product.stock = 5
            >>> product.in_stock
            True
        """
        return self.stock > 0

    def decrease_stock(self, quantity: int) -> None:
        """
        Decrease product stock by specified quantity.

        Args:
            quantity: Amount to decrease

        Raises:
            ValidationError: If insufficient stock

        Example:
            >>> product.stock = 10
            >>> product.decrease_stock(3)
            >>> product.stock
            7
        """
        if quantity < 0:
            raise ValidationError("Quantity must be positive.")

        if self.stock < quantity:
            raise ValidationError(
                f"Insufficient stock. Available: {self.stock}, "
                f"Requested: {quantity}"
            )

        self.stock -= quantity
        self.save(update_fields=["stock", "updated_at"])

    def increase_stock(self, quantity: int) -> None:
        """
        Increase product stock by specified quantity.

        Args:
            quantity: Amount to increase

        Raises:
            ValidationError: If quantity is negative

        Example:
            >>> product.stock = 10
            >>> product.increase_stock(5)
            >>> product.stock
            15
        """
        if quantity < 0:
            raise ValidationError("Quantity must be positive.")

        self.stock += quantity
        self.save(update_fields=["stock", "updated_at"])

