# Comercio - Sistema de Kiosco

Sistema de punto de venta (POS) diseñado específicamente para kioscos, con interfaz intuitiva y gestión completa de ventas, productos, stock y caja. Construido con Django (backend) y Next.js (frontend).

## ✨ Características Principales

- 🛒 **Punto de Venta Rápido**: Interfaz optimizada para ventas ágiles con soporte de escáner de códigos de barras
- 📦 **Gestión de Productos**: Control completo de inventario con categorías y stock en tiempo real
- 💰 **Control de Caja**: Apertura/cierre de caja con conciliación automática
- 💳 **Múltiples Métodos de Pago**: Efectivo, tarjeta y otros medios
- 📊 **Reportes en Tiempo Real**: Visualización de ventas y métricas del día
- 🎨 **Interfaz Táctil**: Diseñada para uso fácil incluso sin experiencia en computadoras

## 🚀 Tecnologías

### Backend
- Django 5.0
- Django REST Framework
- Python 3.12+
- SQLite (desarrollo) / PostgreSQL (producción)
- Docker & Docker Compose

### Frontend
- Next.js 14 (App Router)
- React 18
- TypeScript
- Tailwind CSS
- shadcn/ui
- Axios

## 📁 Estructura del Proyecto

```
comercio/
├── backend/          # API Django REST Framework
│   ├── config/      # Configuración del proyecto
│   ├── apps/        # Aplicaciones Django
│   └── manage.py    # Utilidad de Django
│
├── frontend/        # Aplicación Next.js
│   ├── src/         # Código fuente
│   │   ├── app/    # Pages y layouts (App Router)
│   │   └── lib/    # Utilidades y configuraciones
│   └── public/      # Archivos estáticos
│
└── README.md        # Este archivo
```

## 🛠️ Instalación

### Opción 1: Docker (Recomendado)

La forma más rápida de ejecutar el proyecto:

```bash
# Clonar el repositorio
git clone https://github.com/gastonfr24/comercio.git
cd comercio

# Desarrollo (SQLite)
docker-compose -f docker-compose.dev.yml up --build

# Producción (PostgreSQL)
docker-compose up --build
```

**URLs:**
- Backend: `http://localhost:8000`
- Frontend: `http://localhost:3000`
- Admin: `http://localhost:8000/admin/`

### Opción 2: Instalación Manual

#### Backend (Django)

1. Navegar a la carpeta backend:
```bash
cd backend
```

2. Crear y activar entorno virtual:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
```bash
copy .env.example .env
# Editar .env con tus configuraciones
```

5. Ejecutar migraciones:
```bash
python manage.py migrate
```

6. Crear superusuario:
```bash
python manage.py createsuperuser
```

7. Ejecutar servidor:
```bash
python manage.py runserver
```

El backend estará disponible en: `http://localhost:8000`

### Frontend (Next.js)

1. Navegar a la carpeta frontend:
```bash
cd frontend
```

2. Instalar dependencias:
```bash
npm install
```

3. Configurar variables de entorno:
```bash
copy .env.local.example .env.local
# Editar .env.local si es necesario
```

4. Ejecutar servidor de desarrollo:
```bash
npm run dev
```

El frontend estará disponible en: `http://localhost:3000`

## 🎯 Endpoints API

### Backend
- **Admin Panel**: `http://localhost:8000/admin/`
- **Health Check**: `http://localhost:8000/api/health/`
- **Products API**: `http://localhost:8000/api/products/`
- **Sales API**: `http://localhost:8000/api/sales/`
- **Cash Register API**: `http://localhost:8000/api/cash-register/`
- **Reports API**: `http://localhost:8000/api/reports/`

### Frontend
- **POS (Punto de Venta)**: `http://localhost:3000/pos`
- **Productos**: `http://localhost:3000/products`
- **Caja**: `http://localhost:3000/cash`
- **Reportes**: `http://localhost:3000/reports`

## 📚 Documentación

Para más información sobre el proyecto, consulta la carpeta `docs/`:

- **[SETUP.md](SETUP.md)**: Guía completa de instalación y configuración
- **[CONTRIBUTING.md](docs/CONTRIBUTING.md)**: Guía de contribución y estándares
- **[docs/methodology/](docs/methodology/)**: Metodología de desarrollo y sprints
- **[docs/guides/](docs/guides/)**: Guías de código y documentación

## 🔄 Metodología de Desarrollo

Este proyecto sigue estrictas prácticas profesionales:

- ✅ **Git Flow**: Ramas main, dev, feature/*, bugfix/*, hotfix/*
- ✅ **Conventional Commits**: Mensajes de commit estandarizados
- ✅ **Sprints Documentados**: Todo el trabajo organizado en sprints de 2 semanas
- ✅ **Documentación Completa**: Código documentado en inglés con docstrings y JSDoc
- ✅ **Testing**: Tests unitarios y de integración
- ✅ **Code Review**: Pull requests con revisión obligatoria

Ver [`.cursorrules`](.cursorrules) para las reglas completas del proyecto.

## 🤝 Contribuir

Lee la [Guía de Contribución](docs/CONTRIBUTING.md) para conocer el proceso y estándares del proyecto.

**Resumen:**
1. Verifica que existe un sprint activo
2. Busca la tarea en `docs/sprints/sprint-N/user-stories.md`
3. Crea una rama feature desde dev
4. Desarrolla siguiendo los estándares de código
5. Actualiza documentación y tests
6. Crea Pull Request hacia dev

## 📄 Licencia

Este proyecto es privado y está bajo desarrollo activo.

## 👥 Autores

- **Gastón Franco** - [@gastonfr24](https://github.com/gastonfr24)

