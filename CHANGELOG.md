# Changelog

Todos los cambios notables de este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

## [Unreleased]

### Added

- Configuración inicial del proyecto
- Backend Django 5.0 con Django REST Framework
- Frontend Next.js 14 con TypeScript
- Tailwind CSS y shadcn/ui para estilos y componentes
- Docker y Docker Compose para containerización
- Configuración de Git Flow y Conventional Commits
- Estructura de documentación profesional en `docs/`
- Sistema de reglas estrictas en `.cursorrules`
- Reglas específicas de código en `backend/.cursorrules` y `frontend/.cursorrules`
- Health check endpoint en `/api/health/`
- Componentes UI base: Button, Card, Badge
- Sprint 1 planificado y documentado en `docs/sprints/sprint-1/`
  - 5 User Stories (30 story points)
  - 27 tareas técnicas detalladas con estimaciones
  - Documentos: planning.md, user-stories.md, progress.md, retrospective.md
- Reglas obligatorias de trabajo con sprints agregadas a `.cursorrules`
  - TODO el trabajo debe estar en un sprint activo
  - Sistema de checkboxes para tracking de tareas
  - Actualización diaria obligatoria de progress.md
  - Proceso completo documentado en `docs/methodology/sprint-format-guide.md`
- **Sprint 1 - T-001 Completada:** Modelo Product con gestión de inventario
  - App products con modelo Product completo
  - Campos: barcode, name, price, cost, stock, category, is_active
  - Validaciones de barcode y precios
  - Métodos de gestión de stock (increase/decrease)
  - Cálculo automático de profit_margin
  - 16 tests unitarios comprehensivos (100% passing)
  - Django admin configurado con filtros y edición inline
  - Migraciones aplicadas exitosamente
- **Sprint 1 - T-002 Completada:** API REST para productos
  - ProductSerializer completo y ProductListSerializer ligero
  - ProductViewSet con operaciones CRUD completas
  - Filtrado por category e is_active
  - Búsqueda por name y barcode (case-insensitive)
  - Ordenamiento por name, price, stock, created_at
  - Paginación (20 items por página, customizable)
  - django-filter integrado para filtros avanzados
  - 17 tests de API (100% passing)
  - Endpoints: GET /api/products/, POST, GET /api/products/{id}/, PUT, PATCH, DELETE
- **Sprint 1 - T-004 Completada:** Modelos Sale y SaleItem
  - App sales con modelos Sale y SaleItem
  - Sale: total, payment_type (cash/card/transfer), status (pending/completed/cancelled), date
  - SaleItem: product, quantity, unit_price, subtotal (auto-calculado)
  - Métodos: calculate_total(), complete_sale(), cancel_sale()
  - Gestión automática de stock al completar/cancelar ventas
  - Validaciones completas en modelos
  - Django admin configurado con inline editing
  - 24 tests comprehensivos (100% passing)
  - Migraciones creadas y aplicadas
- **Sprint 1 - T-005 Completada:** API REST para ventas
  - SaleSerializer y CreateSaleSerializer para crear ventas
  - SaleViewSet con operaciones CRUD completas
  - Validación automática de stock disponible
  - Descuento automático de stock al completar venta
  - Cancelación de ventas con restauración de stock
  - Filtrado por status, payment_type, date
  - Búsqueda por producto
  - 14 tests de API (100% passing)
  - Endpoints: GET /api/sales/, POST, GET /api/sales/{id}/, POST /api/sales/{id}/cancel/
- **Sprint 1 - T-003 Completada:** API de búsqueda rápida de productos
  - Endpoint optimizado GET /api/products/search/?q={query}
  - Búsqueda por código de barras (exacto, case-insensitive)
  - Búsqueda por nombre de producto (parcial, case-insensitive)
  - Prioridad a coincidencias de código de barras
  - Limita resultados a 10 items para respuesta rápida
  - Solo productos activos en resultados
  - 11 tests de búsqueda (100% passing)
  - Optimizado para uso en POS (< 100ms de respuesta)
- **Sprint 1 - T-006 Completada:** Componente ScannerInput para POS
  - Componente React con TypeScript
  - Input con autofocus para escaneo rápido
  - Detección de tecla Enter para búsqueda
  - Loading states y feedback visual
  - Error handling con mensajes claros
  - Integración con shadcn/ui (Input, Button)
  - Accesibilidad (ARIA labels)
  - Página de prueba /pos creada
  - Lint sin errores
- **Sprint 1 - T-007 Completada:** Componente ProductList para resultados
  - Componente React con TypeScript
  - Grid responsive (1-4 columnas según pantalla)
  - Cards de producto con información completa
  - Botón agregar al carrito
  - Estados: loading, empty, error
  - Integración con API de búsqueda
  - Formato de precios en ARS
  - Stock indicator visual
  - Skeleton loading para UX
  - Página /pos actualizada con búsqueda real
- **Sprint 1 - T-008 Completada:** Hook useCart para gestión del carrito
  - Custom React hook con TypeScript
  - Agregar items al carrito (addItem)
  - Remover items (removeItem)
  - Actualizar cantidades (updateQuantity)
  - Incrementar/Decrementar (incrementItem/decrementItem)
  - Limpiar carrito (clearCart)
  - Cálculo automático de totales
  - Persistencia en localStorage
  - Helpers: isInCart, getItemQuantity
  - Integrado en página /pos
  - Badge de resumen en header

### Changed

- Cambiado python-decouple por django-environ en backend
- Configuración de variables de entorno con archivos .env
- Actualizado docker-compose.dev.yml para usar env_file
- Mejorado api.ts en frontend para usar variables de entorno NEXT_PUBLIC

### Fixed

- Corregido error de ESLint en layout.tsx (falta import React)
- Corregido error de CORS configuration en settings.py
- Agregado Dockerfile.dev para desarrollo con docker-compose
- Creado carpeta migrations en app products

### Documentation

- Guía completa de setup y configuración (SETUP.md)
- Documentación de arquitectura base
- Guías de Git Flow y estrategia de branches
- Plantillas de commits y Pull Requests
- Estándares estrictos de documentación de código
- Guía de documentación del proyecto (DOCUMENTATION_GUIDE.md)
- Ejemplos prácticos de documentación (docs/guides/documentation-examples.md)
- Estándares de documentación de código (docs/guides/code-documentation-standards.md)
- CONTRIBUTING.md con proceso de contribución detallado
- CODE_OF_CONDUCT.md basado en Contributor Covenant

### Configuration

- Git configurado para usuario gastonfr24
- Linters y formateadores: flake8, black, isort, prettier, eslint
- VSCode settings y extensiones recomendadas
- EditorConfig para consistencia entre editores
- Makefile con comandos útiles
- Docker compose para desarrollo y producción
- Variables de entorno configuradas (.env files)

## [0.1.0] - 2025-01-XX

### Added

- Configuración inicial del repositorio
- Estructura base de carpetas backend/frontend
- Configuración de entornos virtuales
- Archivos de configuración Docker
- Linters y formateadores (flake8, black, prettier, eslint)
- Configuración de VSCode
- README y guías de inicio

### Changed

- N/A

### Deprecated

- N/A

### Removed

- N/A

### Fixed

- N/A

### Security

- Configuración de variables de entorno
- .gitignore para archivos sensibles

---

## Notas de Versionado

### Versión Actual

**v0.1.0** - Configuración inicial y estructura base del proyecto

### Próxima Release

**v1.0.0** - Primera versión funcional con:

- Sistema de autenticación completo
- Catálogo de productos básico
- API RESTful documentada
- Frontend funcional con UI moderna

### Roadmap

#### v1.1.0 (Sprint 2)

- Carrito de compras
- Gestión de órdenes
- Panel de administración mejorado

#### v1.2.0 (Sprint 3)

- Sistema de pagos
- Notificaciones por email
- Dashboard de analytics

#### v2.0.0 (Sprint 4+)

- Sistema de recomendaciones
- Búsqueda avanzada
- Multi-idioma

---

## Convenciones de Changelog

### Categorías

- **Added**: Nuevas funcionalidades
- **Changed**: Cambios en funcionalidad existente
- **Deprecated**: Funcionalidades que se eliminarán pronto
- **Removed**: Funcionalidades eliminadas
- **Fixed**: Correcciones de bugs
- **Security**: Correcciones de seguridad

### Formato de Entradas

```markdown
### Added

- feat(scope): descripción del cambio (#PR)
```

### Enlaces a Versiones

[Unreleased]: https://github.com/gastonfr24/comercio/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/gastonfr24/comercio/releases/tag/v0.1.0

---

**Mantenido por:** @gastonfr24  
**Última actualización:** 2025-01-XX
