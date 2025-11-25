# 🚀 Guía de Configuración del Proyecto

Esta guía te ayudará a configurar y ejecutar el proyecto de comercio electrónico.

## 📋 Requisitos Previos

### Para desarrollo local:
- Python 3.10 o superior
- Node.js 18 o superior
- pip (gestor de paquetes de Python)
- npm (gestor de paquetes de Node.js)

### Para desarrollo con Docker:
- Docker Desktop
- Docker Compose

## 🔧 Opción 1: Desarrollo Local (Sin Docker)

### Backend (Django)

1. **Navegar a la carpeta del backend:**
```bash
cd backend
```

2. **Crear y activar entorno virtual:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno:**
El archivo `.env` ya está creado con valores por defecto. Puedes modificarlo si es necesario.

5. **Ejecutar migraciones:**
```bash
python manage.py migrate
```

6. **Crear superusuario (opcional):**
```bash
python manage.py createsuperuser
```

7. **Ejecutar servidor:**
```bash
python manage.py runserver
```

El backend estará disponible en: `http://localhost:8000`

### Frontend (Next.js)

1. **Abrir una nueva terminal y navegar a la carpeta del frontend:**
```bash
cd frontend
```

2. **Instalar dependencias:**
```bash
npm install
```

3. **Configurar variables de entorno:**
El archivo `.env.local` ya está creado. Verifica que apunte al backend correcto.

4. **Ejecutar servidor de desarrollo:**
```bash
npm run dev
```

El frontend estará disponible en: `http://localhost:3000`

## 🐳 Opción 2: Desarrollo con Docker

### Usando Docker Compose (Recomendado)

1. **Levantar todos los servicios (Backend, Frontend y PostgreSQL):**
```bash
docker-compose up -d
```

2. **Ver logs:**
```bash
docker-compose logs -f
```

3. **Detener servicios:**
```bash
docker-compose down
```

### Usando Docker Compose Dev (Solo SQLite)

Para desarrollo más rápido sin PostgreSQL:

```bash
docker-compose -f docker-compose.dev.yml up -d
```

### Comandos útiles de Docker:

```bash
# Ver contenedores en ejecución
docker-compose ps

# Ejecutar comando en el contenedor del backend
docker-compose exec backend python manage.py migrate

# Crear superusuario
docker-compose exec backend python manage.py createsuperuser

# Reiniciar un servicio específico
docker-compose restart backend

# Ver logs de un servicio específico
docker-compose logs -f backend

# Eliminar contenedores y volúmenes
docker-compose down -v
```

## 🔨 Usando el Makefile (Windows/Linux/Mac)

El proyecto incluye un Makefile con comandos útiles:

```bash
# Ver todos los comandos disponibles
make help

# Instalar todas las dependencias
make install

# Levantar con Docker
make docker-up

# Detener Docker
make docker-down

# Limpiar archivos temporales
make clean
```

## 🧪 Testing

### Backend (Django)
```bash
cd backend
python manage.py test

# Con pytest
pytest

# Con coverage
pytest --cov
```

### Frontend (Next.js)
```bash
cd frontend
npm run test  # Cuando agregues tests
```

## 🎨 Linting y Formateo

### Backend
```bash
cd backend

# Flake8 (linting)
flake8 .

# Black (formateo)
black .

# isort (ordenar imports)
isort .
```

### Frontend
```bash
cd frontend

# ESLint
npm run lint

# Prettier (formateo)
npx prettier --write .
```

## 📍 URLs Importantes

### Desarrollo Local:
- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000
- **Django Admin:** http://localhost:8000/admin
- **API Health Check:** http://localhost:8000/api/health/

### Con Docker:
Las mismas URLs aplican, ya que los puertos están mapeados.

## 🗄️ Base de Datos

### SQLite (Por defecto)
El proyecto usa SQLite por defecto para desarrollo rápido. El archivo se crea automáticamente.

### PostgreSQL (Producción)
Para usar PostgreSQL, edita el archivo `.env` del backend:

```env
DB_ENGINE=django.db.backends.postgresql
DB_NAME=comercio_db
DB_USER=postgres
DB_PASSWORD=tu_password
DB_HOST=localhost  # o 'db' si usas Docker
DB_PORT=5432
```

## 🔐 Seguridad

**IMPORTANTE:** Los archivos `.env` incluidos son solo para desarrollo. En producción:

1. Cambia el `SECRET_KEY` de Django
2. Establece `DEBUG=False`
3. Usa contraseñas seguras para la base de datos
4. Configura `ALLOWED_HOSTS` apropiadamente
5. Usa HTTPS

## 🆘 Solución de Problemas

### Error: Puerto 8000 ya está en uso
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Linux/Mac
lsof -i :8000
kill -9 <PID>
```

### Error: Puerto 3000 ya está en uso
```bash
# Cambia el puerto en el comando
cd frontend
npm run dev -- -p 3001
```

### Error: Módulo no encontrado en Python
```bash
# Asegúrate de tener el entorno virtual activado
cd backend
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### Error: Dependencias de Node.js
```bash
cd frontend
rm -rf node_modules
rm package-lock.json
npm install
```

## 📚 Próximos Pasos

1. Crear modelos en Django (`backend/apps/core/models.py`)
2. Crear vistas y serializers para la API
3. Agregar autenticación JWT
4. Crear componentes en el frontend
5. Implementar páginas de productos, carrito, etc.

## 🤝 Contribuir

1. Crea una rama para tu feature
2. Realiza tus cambios
3. Ejecuta los tests
4. Formatea el código (black, prettier)
5. Crea un Pull Request

¡Feliz desarrollo! 🎉

