# 📚 Documentación del Proyecto Comercio

Bienvenido a la documentación oficial del proyecto Comercio. Esta documentación está organizada para que encuentres rápidamente la información que necesitas.

## 📋 Tabla de Contenidos

### 🏗️ [Arquitectura](./architecture/)
Documentación técnica sobre la arquitectura del sistema.

- [Visión General](./architecture/overview.md) - Vista de alto nivel del sistema
- [Arquitectura del Backend](./architecture/backend-architecture.md) - Django REST Framework
- [Arquitectura del Frontend](./architecture/frontend-architecture.md) - Next.js
- [Esquema de Base de Datos](./architecture/database-schema.md) - Modelo de datos
- [Diseño de la API](./architecture/api-design.md) - Especificación de endpoints

### 🔌 [API](./api/)
Documentación de todos los endpoints de la API.

- [Índice de Endpoints](./api/README.md)
- [Autenticación](./api/authentication.md)
- [Productos](./api/products.md)
- [Órdenes](./api/orders.md)
- [Usuarios](./api/users.md)

### 📖 [Guías](./guides/)
Guías prácticas para desarrolladores y usuarios.

- [Inicio Rápido](./guides/getting-started.md) - Primeros pasos
- [Configuración de Desarrollo](./guides/development-setup.md) - Setup local
- [Despliegue](./guides/deployment.md) - Deploy a producción
- [Testing](./guides/testing.md) - Cómo ejecutar y escribir tests
- [Solución de Problemas](./guides/troubleshooting.md) - Problemas comunes

### 🏃 [Sprints](./sprints/)
Documentación de planificación y retrospectivas de sprints.

- [Sprint 1](./sprints/sprint-1/) - Configuración inicial y autenticación
- [Sprint 2](./sprints/sprint-2/) - (Próximamente)

### 🧠 [Decisiones de Arquitectura](./decisions/)
ADRs (Architecture Decision Records) - Decisiones técnicas importantes.

- [ADR-0001: Uso de Django REST Framework](./decisions/0001-use-django-rest-framework.md)
- [ADR-0002: Uso de Next.js App Router](./decisions/0002-use-nextjs-app-router.md)
- [ADR-0003: PostgreSQL como base de datos](./decisions/0003-use-postgresql.md)

### 📝 Documentos Clave

- [CHANGELOG.md](../CHANGELOG.md) - Historial de cambios
- [CONTRIBUTING.md](./CONTRIBUTING.md) - Cómo contribuir al proyecto
- [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) - Código de conducta

## 🚀 Inicio Rápido

Si eres nuevo en el proyecto, te recomendamos seguir este orden:

1. **Lee el [Inicio Rápido](./guides/getting-started.md)** para entender el proyecto
2. **Configura tu entorno** con la [Guía de Desarrollo](./guides/development-setup.md)
3. **Revisa la [Arquitectura](./architecture/overview.md)** para entender el sistema
4. **Lee las [Reglas de Contribución](./CONTRIBUTING.md)** antes de hacer cambios
5. **Consulta la [API](./api/README.md)** cuando necesites integrar

## 🔍 Buscar Documentación

### Por Tema

- **Backend/Django**: Ver [Arquitectura del Backend](./architecture/backend-architecture.md)
- **Frontend/Next.js**: Ver [Arquitectura del Frontend](./architecture/frontend-architecture.md)
- **API/Endpoints**: Ver [Documentación de API](./api/README.md)
- **Base de Datos**: Ver [Esquema de BD](./architecture/database-schema.md)
- **Despliegue**: Ver [Guía de Despliegue](./guides/deployment.md)
- **Testing**: Ver [Guía de Testing](./guides/testing.md)

### Por Rol

#### Desarrollador Backend
1. [Backend Architecture](./architecture/backend-architecture.md)
2. [Database Schema](./architecture/database-schema.md)
3. [API Design](./architecture/api-design.md)
4. [Testing Guide](./guides/testing.md)

#### Desarrollador Frontend
1. [Frontend Architecture](./architecture/frontend-architecture.md)
2. [API Documentation](./api/README.md)
3. [Development Setup](./guides/development-setup.md)

#### DevOps
1. [Deployment Guide](./guides/deployment.md)
2. [Architecture Overview](./architecture/overview.md)
3. [Troubleshooting](./guides/troubleshooting.md)

#### Product Owner / Scrum Master
1. [Sprint Documentation](./sprints/)
2. [CHANGELOG](../CHANGELOG.md)
3. [Architecture Decisions](./decisions/)

## 📐 Estándares de Documentación

Esta documentación sigue los siguientes estándares:

- **Formato**: Markdown (.md)
- **Idioma**: Español (código en inglés)
- **Estructura**: Organizada por tipo de contenido
- **Actualización**: Mantenida junto con el código
- **Versionado**: Controlada por Git

### Convenciones

- Usar emojis para mejor legibilidad 📝
- Incluir ejemplos de código cuando sea posible
- Mantener enlaces actualizados
- Incluir capturas de pantalla donde sea útil
- Actualizar CHANGELOG.md con cada cambio significativo

## 🤝 Contribuir a la Documentación

¿Encontraste algo confuso o faltante? ¡Ayúdanos a mejorar!

1. Lee [CONTRIBUTING.md](./CONTRIBUTING.md)
2. Crea un issue o PR con la mejora
3. Sigue el formato existente
4. Actualiza el índice si agregas nuevos documentos

## 📞 Soporte

Si no encuentras lo que buscas:

1. **Busca** en esta documentación
2. **Consulta** el [Troubleshooting](./guides/troubleshooting.md)
3. **Pregunta** en los issues de GitHub
4. **Contacta** al equipo de desarrollo

## 📊 Estado de la Documentación

| Sección | Estado | Última Actualización |
|---------|--------|---------------------|
| Arquitectura | 🟡 En Progreso | 2024-01-XX |
| API | 🟡 En Progreso | 2024-01-XX |
| Guías | 🟢 Completo | 2024-01-XX |
| Sprints | 🟡 En Progreso | 2024-01-XX |
| Decisiones | 🟢 Completo | 2024-01-XX |

**Leyenda:**
- 🟢 Completo y actualizado
- 🟡 En progreso o parcial
- 🔴 Desactualizado o faltante

## 🔄 Changelog de Documentación

Ver [CHANGELOG.md](../CHANGELOG.md) para cambios en la documentación.

---

**Última actualización:** 2024-01-XX  
**Mantenedores:** @gastonfr24

¿Preguntas? Abre un issue en GitHub.

