# Backend - Django REST API

Este es el backend del proyecto de comercio, construido con Django y Django REST Framework.

## Requisitos

- Python 3.10+
- pip

## Instalación

1. Crear un entorno virtual:
```bash
python -m venv venv
```

2. Activar el entorno virtual:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
```bash
# Copiar el archivo de ejemplo
copy .env.example .env

# Editar .env con tus configuraciones
```

5. Ejecutar migraciones:
```bash
python manage.py migrate
```

6. Crear un superusuario:
```bash
python manage.py createsuperuser
```

7. Ejecutar el servidor:
```bash
python manage.py runserver
```

## Endpoints disponibles

- `http://localhost:8000/admin/` - Panel de administración de Django
- `http://localhost:8000/api/health/` - Health check de la API

## Estructura del proyecto

```
backend/
├── config/              # Configuración principal del proyecto
│   ├── settings.py     # Configuraciones de Django
│   ├── urls.py         # URLs principales
│   ├── wsgi.py         # Configuración WSGI
│   └── asgi.py         # Configuración ASGI
├── apps/               # Aplicaciones del proyecto
│   └── core/          # App principal
│       ├── models.py  # Modelos de datos
│       ├── views.py   # Vistas/Controladores
│       ├── serializers.py  # Serializadores
│       └── urls.py    # URLs de la app
├── manage.py          # Utilidad de línea de comandos
└── requirements.txt   # Dependencias del proyecto
```

## Comandos útiles

```bash
# Crear una nueva app
python manage.py startapp nombre_app

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar tests
python manage.py test

# Recolectar archivos estáticos
python manage.py collectstatic
```

