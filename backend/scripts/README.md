# Scripts de Utilidad

Esta carpeta contiene scripts útiles para el proyecto.

## 📁 Estructura

```
backend/
├── create_superuser.py       # Crear superusuario para desarrollo
├── create_demo_products.py   # Crear productos ficticios para demo
└── scripts/
    └── README.md             # Este archivo
```

## 🚀 Scripts Disponibles

### 1. Crear Superusuario

Crea un superusuario predeterminado para desarrollo.

**Ubicación:** `backend/create_superuser.py`

**Uso:**

```bash
# Desde el directorio backend/
python create_superuser.py

# Con Docker
docker exec comercio_backend_dev python create_superuser.py
```

**Configuración:**

Las credenciales se leen desde el archivo `.env.dev`:

```env
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=admin123
```

**Resultado:**
- Usuario creado: `admin` / `admin123`
- Acceso al admin: `http://localhost:8000/admin`

---

### 2. Crear Productos de Demo

Crea 25 productos ficticios para testing y demostraciones.

**Ubicación:** `backend/create_demo_products.py`

**Uso:**

```bash
# Desde el directorio backend/
python create_demo_products.py

# Con Docker
docker exec comercio_backend_dev python create_demo_products.py
```

**Productos Incluidos:**

- **Bebidas** (6): Coca Cola, Sprite, Fanta, Agua, Cerveza
- **Snacks** (4): Papas, Doritos, Maní, Oreo
- **Golosinas** (5): Alfajores, Chocolates, Caramelos, Chicles
- **Lácteos** (2): Leche, Yogur
- **Cigarrillos** (2): Marlboro, Philip Morris
- **Limpieza** (2): Jabón líquido, Lavandina
- **Varios** (4): Pilas, Encendedor, Yerba mate, etc.

**Casos de Testing:**

- ✅ Productos activos con stock normal
- ⚠️ Productos con stock bajo (< 10 unidades)
- ❌ Productos sin stock (0 unidades)
- 🚫 Productos inactivos

**Características:**

- Si el producto ya existe (por barcode), se actualiza
- Precios realistas en pesos argentinos
- Costos calculados (~70% del precio)
- Categorías diversas

**Resultado:**

```
🛒 CREATING DEMO PRODUCTS FOR KIOSK
============================================================

✨ Created: Coca Cola 500ml
✨ Created: Papas Lays Clasicas 165g
...

============================================================
✅ COMPLETED SUCCESSFULLY
   Created: 25 products
   Updated: 0 products
   Total: 25 products in database
============================================================

📊 Product Summary by Category:
   - Bebidas: 6 products
   - Snacks: 4 products
   - Golosinas: 5 products
   - Lacteos: 2 products
   - Cigarrillos: 2 products
   - Limpieza: 2 products
   - Varios: 3 products
   - Almacen: 1 products

🎯 Quick Stats:
   - Active products: 24
   - Low stock (< 10): 2
   - Out of stock: 1
```

---

## 🔄 Orden de Ejecución Recomendado

Para configurar un entorno de desarrollo completo:

```bash
# 1. Aplicar migraciones
docker exec comercio_backend_dev python manage.py migrate

# 2. Crear superusuario
docker exec comercio_backend_dev python create_superuser.py

# 3. Crear productos de demo
docker exec comercio_backend_dev python create_demo_products.py
```

Ahora puedes:
- Acceder al admin: `http://localhost:8000/admin`
- Probar el POS con productos reales: `http://localhost:3000/pos`
- Ver productos en la API: `http://localhost:8000/api/products/`

---

## ⚙️ Crear Nuevos Scripts

### Template para Scripts

```python
"""
Script description.

Usage:
    python script_name.py
"""

import os
import sys
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# Your imports here
from apps.products.models import Product


def main():
    """
    Main function.
    """
    print("Script running...")
    
    # Your logic here
    
    print("Completed!")


if __name__ == "__main__":
    main()
```

### Ubicación

- Scripts principales: `backend/` (raíz)
- Scripts auxiliares: `backend/scripts/`

### Convenciones

1. **Nomenclatura:** `snake_case.py`
2. **Docstring:** Descripción y uso al inicio
3. **Main function:** Siempre incluir `if __name__ == "__main__"`
4. **Django setup:** Importar y configurar Django al inicio
5. **Output:** Usar emojis para claridad visual
6. **Error handling:** Try/catch y `sys.exit(1)` en errores

---

## 📝 Notas

- Estos scripts están diseñados para **desarrollo y testing**
- No ejecutar en producción sin revisar
- Los datos de demo son ficticios
- Los scripts son **idempotentes** (se pueden ejecutar múltiples veces)

---

**Última actualización:** 27/11/2025  
**Mantenedor:** @gastonfr24

