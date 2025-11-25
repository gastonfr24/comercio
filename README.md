# Comercio - E-commerce Platform

Plataforma completa de comercio electrónico construida con Django (backend) y Next.js (frontend).

## 🚀 Tecnologías

### Backend
- Django 5.0
- Django REST Framework
- Python 3.10+
- SQLite (desarrollo) / PostgreSQL (producción)

### Frontend
- Next.js 14
- React 18
- TypeScript
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

### Backend (Django)

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

## 🎯 Endpoints disponibles

### Backend
- Admin: `http://localhost:8000/admin/`
- API Health Check: `http://localhost:8000/api/health/`

### Frontend
- Página principal: `http://localhost:3000`

## 📝 Próximos pasos

### Backend
- [ ] Crear modelos de datos (Productos, Usuarios, Órdenes, etc.)
- [ ] Implementar autenticación JWT
- [ ] Crear endpoints RESTful para el CRUD
- [ ] Implementar permisos y roles
- [ ] Agregar paginación y filtros
- [ ] Configurar PostgreSQL para producción

### Frontend
- [ ] Crear páginas principales (Home, Productos, Carrito, Perfil)
- [ ] Implementar sistema de autenticación
- [ ] Crear componentes reutilizables
- [ ] Agregar gestión de estado
- [ ] Implementar carrito de compras
- [ ] Agregar procesamiento de pagos

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.

## 👥 Autores

Tu nombre aquí

## 📧 Contacto

Tu email aquí

