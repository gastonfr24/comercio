# 📚 Guía de Documentación del Proyecto

Este documento es tu guía rápida para mantener la documentación del proyecto actualizada y consistente.

## 🗂️ Estructura de Documentación

```
comercio/
├── .cursorrules                    # Reglas principales de Cursor
├── CHANGELOG.md                    # Historial de cambios (OBLIGATORIO actualizar)
├── README.md                       # Documentación general del proyecto
├── DOCUMENTATION_GUIDE.md          # Este archivo
│
├── backend/
│   ├── .cursorrules               # Reglas específicas de Python/Django
│   └── README.md                  # Documentación del backend
│
├── frontend/
│   ├── .cursorrules               # Reglas específicas de TypeScript/React
│   └── README.md                  # Documentación del frontend
│
└── docs/                          # Documentación principal
    ├── README.md                  # Índice de documentación
    ├── CONTRIBUTING.md            # Guía de contribución
    ├── CODE_OF_CONDUCT.md         # Código de conducta
    │
    ├── architecture/              # Arquitectura del sistema
    │   ├── overview.md
    │   ├── backend-architecture.md
    │   ├── frontend-architecture.md
    │   ├── database-schema.md
    │   └── api-design.md
    │
    ├── api/                       # Documentación de API
    │   ├── README.md
    │   ├── authentication.md
    │   ├── products.md
    │   ├── orders.md
    │   └── users.md
    │
    ├── guides/                    # Guías prácticas
    │   ├── getting-started.md
    │   ├── development-setup.md
    │   ├── deployment.md
    │   ├── testing.md
    │   ├── code-documentation-standards.md
    │   └── troubleshooting.md
    │
    ├── sprints/                   # Documentación de sprints
    │   ├── sprint-1/
    │   │   ├── planning.md
    │   │   ├── user-stories.md
    │   │   └── retrospective.md
    │   └── sprint-2/
    │
    └── decisions/                 # Architecture Decision Records
        ├── 0001-use-django-rest-framework.md
        ├── 0002-use-nextjs-app-router.md
        └── 0003-use-postgresql.md
```

## 📝 ¿Qué documentar y cuándo?

### SIEMPRE Documentar

1. **Funciones públicas en código** (docstrings/JSDoc)
2. **APIs y endpoints** (en `docs/api/`)
3. **Cambios en CHANGELOG.md** (con cada feature/fix)
4. **Decisiones de arquitectura** (ADRs en `docs/decisions/`)
5. **Setup y configuración** (actualizar guías)

### Documentar CUANDO sea necesario

1. **Algoritmos complejos** (comentarios explicativos)
2. **Decisiones de diseño** no obvias
3. **Integraciones externas** (APIs de terceros)
4. **Configuraciones especiales** (variables de entorno)

### NUNCA Documentar

1. **Código obvio** (no agregar ruido)
2. **Historial de cambios en comentarios** (usar Git)
3. **TODO sin issue asociado** (crear issue primero)
4. **Información desactualizada** (eliminar si no se actualiza)

## 🔄 Workflow de Documentación

### Al crear una nueva feature

```bash
# 1. Documentar código (docstrings/JSDoc)
# Mientras escribes el código

# 2. Actualizar CHANGELOG.md
## [Unreleased]
### Added
- feat(products): add product filtering by category

# 3. Actualizar docs de API si aplica
# docs/api/products.md

# 4. Commit con conventional commits
git commit -m "feat(products): add product filtering by category"
```

### Al corregir un bug

```bash
# 1. Asegurar que el código esté documentado

# 2. Actualizar CHANGELOG.md
## [Unreleased]
### Fixed
- fix(cart): resolve decimal precision error in totals

# 3. Commit
git commit -m "fix(cart): resolve decimal precision error in totals"
```

### Al tomar decisión de arquitectura

```bash
# 1. Crear ADR en docs/decisions/
# docs/decisions/0004-use-redis-for-caching.md

# 2. Actualizar arquitectura si aplica
# docs/architecture/backend-architecture.md

# 3. Actualizar CHANGELOG.md
## [Unreleased]
### Changed
- Implemented Redis caching layer (see ADR-0004)

# 4. Commit
git commit -m "docs(arch): add ADR for Redis caching decision"
```

### Al finalizar un sprint

```bash
# 1. Documentar retrospectiva
# docs/sprints/sprint-X/retrospective.md

# 2. Preparar release notes desde CHANGELOG.md

# 3. Actualizar versión
## [1.1.0] - 2024-XX-XX

# 4. Tag de release
git tag -a v1.1.0 -m "Release version 1.1.0"
```

## 📋 Plantillas Rápidas

### Docstring Python

```python
def function_name(param1: Type1, param2: Type2) -> ReturnType:
    """
    Brief description of what the function does.
    
    More detailed explanation if needed. Can be multiple lines.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of what is returned
        
    Raises:
        ExceptionType: When this exception is raised
        
    Example:
        >>> function_name(value1, value2)
        expected_result
    """
    pass
```

### JSDoc TypeScript

```typescript
/**
 * Brief description of what the function/component does.
 * 
 * More detailed explanation if needed.
 * 
 * @param param1 - Description of param1
 * @param param2 - Description of param2
 * @returns Description of what is returned
 * @throws {ErrorType} When this error is thrown
 * 
 * @example
 * ```ts
 * functionName(value1, value2)
 * // expected_result
 * ```
 */
```

### Entrada en CHANGELOG.md

```markdown
## [Unreleased]

### Added
- feat(scope): descripción breve del cambio (#PR)

### Changed
- refactor(scope): descripción breve del cambio (#PR)

### Fixed
- fix(scope): descripción breve del cambio (#PR)

### Security
- security(scope): descripción breve del cambio (#PR)
```

### Architecture Decision Record (ADR)

```markdown
# ADR-XXXX: Título de la Decisión

**Fecha:** YYYY-MM-DD  
**Estado:** [Propuesto | Aceptado | Rechazado | Deprecado | Reemplazado por ADR-YYYY]  
**Contexto:** [Sprint X]

## Contexto y Problema

[Describe el contexto y el problema que motiva esta decisión]

## Opciones Consideradas

1. **Opción 1:** [Descripción]
   - ✅ Pros: ...
   - ❌ Contras: ...

2. **Opción 2:** [Descripción]
   - ✅ Pros: ...
   - ❌ Contras: ...

## Decisión

[Opción elegida y justificación]

## Consecuencias

### Positivas
- [Consecuencia positiva 1]
- [Consecuencia positiva 2]

### Negativas
- [Consecuencia negativa 1]
- [Consecuencia negativa 2]

### Riesgos
- [Riesgo 1 y plan de mitigación]

## Implementación

- [ ] Tarea 1
- [ ] Tarea 2

## Referencias

- [Link a issue]
- [Link a documentación externa]
```

## ✅ Checklist de Documentación

Antes de hacer merge a `dev`:

- [ ] Código tiene docstrings/JSDoc apropiados
- [ ] CHANGELOG.md está actualizado
- [ ] API docs actualizados (si aplica)
- [ ] README actualizado (si aplica)
- [ ] ADR creado para decisiones importantes
- [ ] Guías actualizadas (si cambió setup/deployment)
- [ ] Sin comentarios con emojis
- [ ] Sin código comentado
- [ ] Sin historial en comentarios
- [ ] TODOs tienen issue asociado

## 🎯 Niveles de Prioridad

### 🔴 Crítico - Debe estar antes del merge
- Docstrings en funciones públicas
- CHANGELOG.md actualizado
- API docs para nuevos endpoints

### 🟡 Importante - Debe estar antes del release
- ADRs para decisiones arquitectónicas
- Guías actualizadas
- Documentación de sprints

### 🟢 Nice to have - Puede ser después
- Ejemplos adicionales
- Diagramas de arquitectura
- Videos tutoriales

## 🚫 Qué NO hacer

❌ **Nunca** commitear sin actualizar CHANGELOG.md  
❌ **Nunca** usar emojis en comentarios de código  
❌ **Nunca** dejar código comentado "por si acaso"  
❌ **Nunca** poner historial de cambios en comentarios  
❌ **Nunca** usar TODO sin issue de GitHub  
❌ **Nunca** documentar código obvio  
❌ **Nunca** dejar documentación desactualizada  

## 📞 ¿Dudas?

1. **Sobre formato:** Lee esta guía y `.cursorrules`
2. **Sobre contenido:** Revisa ejemplos en `docs/`
3. **Sobre arquitectura:** Consulta `docs/architecture/`
4. **Sobre API:** Consulta `docs/api/`
5. **Aún con dudas:** Crea un issue con etiqueta `documentation`

## 🔗 Enlaces Rápidos

- [.cursorrules principal](./.cursorrules)
- [Backend rules](./backend/.cursorrules)
- [Frontend rules](./frontend/.cursorrules)
- [CHANGELOG.md](./CHANGELOG.md)
- [CONTRIBUTING.md](./docs/CONTRIBUTING.md)
- [Code Documentation Standards](./docs/guides/code-documentation-standards.md)

---

**Última actualización:** 2025-01-XX  
**Mantenedores:** @gastonfr24

*"La documentación es amor por tu yo futuro y por tus compañeros de equipo"*

