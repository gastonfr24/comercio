"""
Models for sales app.
"""

from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from apps.products.models import Product


class Sale(models.Model):
    """
    Sale model representing a complete transaction.

    Attributes:
        total: Total amount of the sale
        payment_type: Type of payment (cash, card, transfer)
        date: Date and time of the sale
        status: Status of the sale (pending, completed, cancelled)
    """

    PAYMENT_TYPES = [
        ("cash", "Efectivo"),
        ("card", "Tarjeta"),
        ("transfer", "Transferencia"),
    ]

    STATUS_CHOICES = [
        ("pending", "Pendiente"),
        ("completed", "Completada"),
        ("cancelled", "Cancelada"),
    ]

    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))],
        help_text="Total amount of the sale",
    )
    payment_type = models.CharField(
        max_length=20,
        choices=PAYMENT_TYPES,
        default="cash",
        help_text="Payment method used",
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
        help_text="Current status of the sale",
    )
    date = models.DateTimeField(auto_now_add=True, help_text="Date and time of sale")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date"]
        verbose_name = "Sale"
        verbose_name_plural = "Sales"
        indexes = [
            models.Index(fields=["-date"]),
            models.Index(fields=["status"]),
            models.Index(fields=["payment_type"]),
        ]

    def __str__(self):
        """
        String representation of Sale.

        Returns:
            String with sale ID and total
        """
        return f"Sale #{self.id} - ${self.total}"

    def calculate_total(self):
        """
        Calculate total from sale items.

        Returns:
            Total calculated from all sale items

        Example:
            >>> sale.calculate_total()
            Decimal('150.50')
        """
        total = sum(item.subtotal for item in self.items.all())
        return Decimal(str(total)).quantize(Decimal("0.01"))

    def complete_sale(self):
        """
        Mark sale as completed and update product stock.

        Raises:
            ValidationError: If sale is not pending or stock is insufficient
        """
        if self.status != "pending":
            raise ValidationError(
                f"Cannot complete sale with status '{self.status}'. Must be 'pending'."
            )

        # Decrementar stock de cada producto
        for item in self.items.all():
            item.product.decrease_stock(item.quantity)

        self.status = "completed"
        self.save()

    def cancel_sale(self):
        """
        Cancel a pending sale and restore stock if it was completed.

        Raises:
            ValidationError: If sale is already cancelled
        """
        if self.status == "cancelled":
            raise ValidationError("Sale is already cancelled.")

        # Si estaba completada, devolver el stock
        if self.status == "completed":
            for item in self.items.all():
                item.product.increase_stock(item.quantity)

        self.status = "cancelled"
        self.save()

    def clean(self):
        """
        Validate sale data.
        """
        super().clean()

        if self.total is not None and self.total <= 0:
            raise ValidationError({"total": "Total must be greater than zero."})

    def save(self, *args, **kwargs):
        """
        Save sale with validation.
        """
        self.full_clean()
        super().save(*args, **kwargs)


class SaleItem(models.Model):
    """
    SaleItem model representing individual items in a sale.

    Attributes:
        sale: Foreign key to Sale
        product: Foreign key to Product
        quantity: Quantity of product sold
        unit_price: Price per unit at time of sale
        subtotal: Calculated subtotal (quantity * unit_price)
    """

    sale = models.ForeignKey(
        Sale, on_delete=models.CASCADE, related_name="items", help_text="Related sale"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="sale_items",
        help_text="Product sold",
    )
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)], help_text="Quantity sold"
    )
    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))],
        help_text="Unit price at time of sale",
    )
    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))],
        help_text="Subtotal (quantity * unit_price)",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Sale Item"
        verbose_name_plural = "Sale Items"
        ordering = ["id"]
        indexes = [
            models.Index(fields=["sale"]),
            models.Index(fields=["product"]),
        ]

    def __str__(self):
        """
        String representation of SaleItem.

        Returns:
            String with product name and quantity
        """
        return f"{self.quantity}x {self.product.name}"

    def calculate_subtotal(self):
        """
        Calculate subtotal from quantity and unit price.

        Returns:
            Calculated subtotal

        Example:
            >>> item.calculate_subtotal()
            Decimal('30.00')
        """
        return (Decimal(str(self.quantity)) * self.unit_price).quantize(Decimal("0.01"))

    def clean(self):
        """
        Validate sale item data.
        """
        super().clean()

        if self.quantity is not None and self.quantity <= 0:
            raise ValidationError({"quantity": "Quantity must be greater than zero."})

        if self.unit_price is not None and self.unit_price <= 0:
            raise ValidationError(
                {"unit_price": "Unit price must be greater than zero."}
            )

        # Validar que el producto esté activo
        if self.product and not self.product.is_active:
            raise ValidationError(
                {"product": f"Product '{self.product.name}' is not active."}
            )

        # Validar que haya stock suficiente (solo en creación)
        if self.product and not self.pk:  # Solo en creación
            if not self.product.in_stock or self.product.stock < self.quantity:
                raise ValidationError(
                    {"quantity": f"Insufficient stock. Available: {self.product.stock}"}
                )

    def save(self, *args, **kwargs):
        """
        Save sale item with automatic subtotal calculation.
        """
        # Calcular subtotal automáticamente
        if self.quantity and self.unit_price:
            self.subtotal = self.calculate_subtotal()

        self.full_clean()
        super().save(*args, **kwargs)
