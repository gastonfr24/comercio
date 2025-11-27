"""
Script to create demo products for testing and demonstrations.

Run this script after running migrations:
    python create_demo_products.py
"""

import os
import sys
import django
from decimal import Decimal

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.products.models import Product


def create_demo_products():
    """
    Creates a set of realistic demo products for a kiosk/convenience store.
    
    Returns:
        int: Number of products created
    """
    
    demo_products = [
        # Bebidas
        {
            "barcode": "7790310981801",
            "name": "Coca Cola 500ml",
            "price": Decimal("450.00"),
            "cost": Decimal("320.00"),
            "stock": 50,
            "category": "Bebidas",
            "is_active": True,
        },
        {
            "barcode": "7790310981818",
            "name": "Coca Cola 1.5L",
            "price": Decimal("850.00"),
            "cost": Decimal("620.00"),
            "stock": 30,
            "category": "Bebidas",
            "is_active": True,
        },
        {
            "barcode": "7790895000072",
            "name": "Agua Mineral Villavicencio 500ml",
            "price": Decimal("350.00"),
            "cost": Decimal("240.00"),
            "stock": 60,
            "category": "Bebidas",
            "is_active": True,
        },
        {
            "barcode": "7790742011114",
            "name": "Sprite 500ml",
            "price": Decimal("450.00"),
            "cost": Decimal("320.00"),
            "stock": 40,
            "category": "Bebidas",
            "is_active": True,
        },
        {
            "barcode": "7790070302182",
            "name": "Fanta 500ml",
            "price": Decimal("450.00"),
            "cost": Decimal("320.00"),
            "stock": 35,
            "category": "Bebidas",
            "is_active": True,
        },
        {
            "barcode": "7790895000515",
            "name": "Cerveza Quilmes 1L",
            "price": Decimal("950.00"),
            "cost": Decimal("680.00"),
            "stock": 25,
            "category": "Bebidas",
            "is_active": True,
        },
        
        # Snacks
        {
            "barcode": "7622210449283",
            "name": "Oreo Original 118g",
            "price": Decimal("680.00"),
            "cost": Decimal("480.00"),
            "stock": 45,
            "category": "Snacks",
            "is_active": True,
        },
        {
            "barcode": "7790040555518",
            "name": "Papas Lays Clasicas 165g",
            "price": Decimal("890.00"),
            "cost": Decimal("620.00"),
            "stock": 50,
            "category": "Snacks",
            "is_active": True,
        },
        {
            "barcode": "7790040555525",
            "name": "Doritos Nacho 150g",
            "price": Decimal("920.00"),
            "cost": Decimal("650.00"),
            "stock": 40,
            "category": "Snacks",
            "is_active": True,
        },
        {
            "barcode": "7891000100103",
            "name": "Mani Lider Salado 100g",
            "price": Decimal("520.00"),
            "cost": Decimal("360.00"),
            "stock": 55,
            "category": "Snacks",
            "is_active": True,
        },
        
        # Golosinas
        {
            "barcode": "7790580111205",
            "name": "Alfajor Jorgito Triple",
            "price": Decimal("420.00"),
            "cost": Decimal("290.00"),
            "stock": 70,
            "category": "Golosinas",
            "is_active": True,
        },
        {
            "barcode": "7790580111229",
            "name": "Alfajor Guaymallen Triple",
            "price": Decimal("380.00"),
            "cost": Decimal("260.00"),
            "stock": 80,
            "category": "Golosinas",
            "is_active": True,
        },
        {
            "barcode": "7622210449306",
            "name": "Chocolatinas Milka 100g",
            "price": Decimal("990.00"),
            "cost": Decimal("720.00"),
            "stock": 30,
            "category": "Golosinas",
            "is_active": True,
        },
        {
            "barcode": "7790040211049",
            "name": "Caramelos Sugus Surtidos 150g",
            "price": Decimal("650.00"),
            "cost": Decimal("450.00"),
            "stock": 40,
            "category": "Golosinas",
            "is_active": True,
        },
        {
            "barcode": "7622210449313",
            "name": "Chicles Beldent x10",
            "price": Decimal("280.00"),
            "cost": Decimal("190.00"),
            "stock": 100,
            "category": "Golosinas",
            "is_active": True,
        },
        
        # Lacteos
        {
            "barcode": "7790387005011",
            "name": "Leche La Serenisima 1L",
            "price": Decimal("750.00"),
            "cost": Decimal("560.00"),
            "stock": 25,
            "category": "Lacteos",
            "is_active": True,
        },
        {
            "barcode": "7790387005028",
            "name": "Yogur Ser Frutilla 190g",
            "price": Decimal("420.00"),
            "cost": Decimal("290.00"),
            "stock": 35,
            "category": "Lacteos",
            "is_active": True,
        },
        
        # Cigarrillos
        {
            "barcode": "7790742000016",
            "name": "Cigarrillos Marlboro Box",
            "price": Decimal("1450.00"),
            "cost": Decimal("1120.00"),
            "stock": 20,
            "category": "Cigarrillos",
            "is_active": True,
        },
        {
            "barcode": "7790742000023",
            "name": "Cigarrillos Philip Morris Box",
            "price": Decimal("1380.00"),
            "cost": Decimal("1080.00"),
            "stock": 18,
            "category": "Cigarrillos",
            "is_active": True,
        },
        
        # Productos de limpieza
        {
            "barcode": "7790070301123",
            "name": "Jabon Liquido Skip 500ml",
            "price": Decimal("1250.00"),
            "cost": Decimal("920.00"),
            "stock": 15,
            "category": "Limpieza",
            "is_active": True,
        },
        {
            "barcode": "7790070301130",
            "name": "Lavandina Ayudin 1L",
            "price": Decimal("680.00"),
            "cost": Decimal("480.00"),
            "stock": 20,
            "category": "Limpieza",
            "is_active": True,
        },
        
        # Productos con bajo stock (para testing)
        {
            "barcode": "7790070301147",
            "name": "Pilas Duracell AA x4",
            "price": Decimal("1850.00"),
            "cost": Decimal("1350.00"),
            "stock": 8,
            "category": "Varios",
            "is_active": True,
        },
        {
            "barcode": "7790070301154",
            "name": "Encendedor BIC",
            "price": Decimal("350.00"),
            "cost": Decimal("220.00"),
            "stock": 5,
            "category": "Varios",
            "is_active": True,
        },
        
        # Producto sin stock (para testing)
        {
            "barcode": "7790070301161",
            "name": "Yerba Mate Rosamonte 1kg",
            "price": Decimal("2850.00"),
            "cost": Decimal("2150.00"),
            "stock": 0,
            "category": "Almacen",
            "is_active": True,
        },
        
        # Producto inactivo (para testing)
        {
            "barcode": "7790070301178",
            "name": "Producto Descontinuado",
            "price": Decimal("100.00"),
            "cost": Decimal("50.00"),
            "stock": 10,
            "category": "Varios",
            "is_active": False,
        },
    ]
    
    created_count = 0
    updated_count = 0
    
    for product_data in demo_products:
        barcode = product_data["barcode"]
        
        # Check if product already exists
        existing_product = Product.objects.filter(barcode=barcode).first()
        
        if existing_product:
            # Update existing product
            for key, value in product_data.items():
                setattr(existing_product, key, value)
            existing_product.save()
            updated_count += 1
            print(f"✅ Updated: {product_data['name']}")
        else:
            # Create new product
            Product.objects.create(**product_data)
            created_count += 1
            print(f"✨ Created: {product_data['name']}")
    
    return created_count, updated_count


def main():
    """
    Main function to execute the script.
    """
    print("=" * 60)
    print("🛒 CREATING DEMO PRODUCTS FOR KIOSK")
    print("=" * 60)
    print()
    
    try:
        created, updated = create_demo_products()
        
        print()
        print("=" * 60)
        print(f"✅ COMPLETED SUCCESSFULLY")
        print(f"   Created: {created} products")
        print(f"   Updated: {updated} products")
        print(f"   Total: {Product.objects.count()} products in database")
        print("=" * 60)
        print()
        print("📊 Product Summary by Category:")
        
        categories = Product.objects.values_list("category", flat=True).distinct()
        for category in categories:
            count = Product.objects.filter(category=category).count()
            print(f"   - {category}: {count} products")
        
        print()
        print("🎯 Quick Stats:")
        active_count = Product.objects.filter(is_active=True).count()
        low_stock_count = Product.objects.filter(stock__lt=10, is_active=True).count()
        out_of_stock_count = Product.objects.filter(stock=0, is_active=True).count()
        
        print(f"   - Active products: {active_count}")
        print(f"   - Low stock (< 10): {low_stock_count}")
        print(f"   - Out of stock: {out_of_stock_count}")
        print()
        
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()

