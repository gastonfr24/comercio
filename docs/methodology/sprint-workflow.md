# 🏃 Metodología de Trabajo con Sprints

## 🎯 Filosofía de Trabajo

Este proyecto sigue **Scrum** adaptado para equipos pequeños con énfasis en:

- **Sprints de 2 semanas**
- **Una tarea = Una rama = Un Pull Request**
- **Desarrollo incremental y funcional**
- **Entrega continua de valor**

---

## 📅 Ciclo de Sprint (2 Semanas)

```
Semana 1                          Semana 2
├─────────────┬─────────────────┬─────────────┬─────────────────┤
│   Día 1-2   │     Día 3-7     │   Día 8-9   │    Día 10-14    │
├─────────────┼─────────────────┼─────────────┼─────────────────┤
│  Planning   │   Development   │   Testing   │   Review/Demo   │
│  & Setup    │   & Daily Work  │   & Fixes   │   & Retro       │
└─────────────┴─────────────────┴─────────────┴─────────────────┘
```

### Día 1-2: Sprint Planning

- **Sprint Planning Meeting (2-4 horas)**

  - Revisar y priorizar backlog
  - Seleccionar user stories para el sprint
  - Descomponer en tareas técnicas
  - Estimar story points
  - Definir Definition of Done
  - Asignar tareas iniciales

- **Entregables:**
  - `docs/sprints/sprint-N/planning.md` creado
  - `docs/sprints/sprint-N/user-stories.md` creado
  - Ramas feature/\* creadas desde `dev`
  - GitHub Issues creados y etiquetados

### Día 3-9: Development

- **Daily Standup (15 min cada día)**

  - ¿Qué hice ayer?
  - ¿Qué haré hoy?
  - ¿Tengo impedimentos?

- **Trabajo diario:**
  - Desarrollar en rama feature/\*
  - Commits frecuentes con Conventional Commits
  - Actualizar CHANGELOG.md
  - Tests unitarios
  - Code reviews

### Día 10-12: Testing & Refinement

- Testing integración
- Corrección de bugs
- Refinamiento de features
- Actualización de documentación

### Día 13-14: Review & Retrospective

- **Sprint Review (1-2 horas)**

  - Demo de funcionalidades completadas
  - Feedback del Product Owner/Cliente
  - Aceptación de user stories

- **Sprint Retrospective (1 hora)**

  - ¿Qué funcionó bien?
  - ¿Qué no funcionó?
  - ¿Qué mejorar para el siguiente sprint?
  - Acciones concretas

- **Sprint Closure:**
  - Merge de todas las features aprobadas a `dev`
  - Actualizar documentación
  - Cerrar sprint en `docs/sprints/sprint-N/retrospective.md`
  - Tag de versión si corresponde

---

## 📋 De User Story a Código

### Paso 1: User Story

```markdown
## US-001: Registro rápido de venta

**Como** cajero del kiosco
**Quiero** registrar ventas escaneando productos
**Para** cobrar de forma rápida y sin errores

**Criterios de Aceptación:**

- [ ] Puedo escanear código de barras
- [ ] Se muestra el producto y precio
- [ ] Se acumula el total automáticamente
- [ ] Puedo eliminar un item si me equivoqué
- [ ] El proceso toma menos de 30 segundos

**Story Points:** 8
**Prioridad:** Alta
**Sprint:** Sprint 1
```

### Paso 2: Descomponer en Tareas Técnicas

```markdown
### Tareas para US-001:

**Backend:**

- [ ] T-001: Crear modelo Product con código de barras
- [ ] T-002: API endpoint para buscar producto por código
- [ ] T-003: Crear modelo Sale y SaleItem
- [ ] T-004: API endpoint para crear venta
- [ ] T-005: Tests unitarios de modelos y APIs

**Frontend:**

- [ ] T-006: Componente ScannerInput
- [ ] T-007: Componente ProductList en venta
- [ ] T-008: Componente SaleTotal
- [ ] T-009: Lógica de estado de venta (hook)
- [ ] T-010: Tests de componentes

**Integración:**

- [ ] T-011: Integrar escáner con API
- [ ] T-012: Manejo de errores
- [ ] T-013: Testing E2E del flujo completo
```

### Paso 3: Cada Tarea = Una Rama

```bash
# T-001: Crear modelo Product
git checkout dev
git pull origin dev
git checkout -b feature/sprint1-001-product-model

# Trabajar en la tarea
# Commits frecuentes
git commit -m "feat(products): add Product model with barcode field"
git commit -m "feat(products): add barcode validation"
git commit -m "test(products): add Product model tests"

# Push y crear PR
git push origin feature/sprint1-001-product-model
```

### Paso 4: Pull Request

````markdown
## 📋 Tarea: T-001 - Modelo Product con código de barras

**User Story:** US-001 - Registro rápido de venta
**Sprint:** Sprint 1

## 🎯 Descripción

Implementa el modelo Product con soporte para códigos de barras,
validación de formato, y campos necesarios para el sistema de kiosco.

## ✅ Checklist

- [x] Modelo Product creado
- [x] Campo barcode con validación
- [x] Tests unitarios (coverage >80%)
- [x] Documentación actualizada
- [x] CHANGELOG.md actualizado

## 🧪 Testing

```bash
pytest apps/products/tests/test_models.py
```
````

## 🔗 Relacionado

- Parte de US-001
- Issue #15

````

### Paso 5: Actualizar Documentación (OBLIGATORIO)

**SIEMPRE antes de crear el PR, actualizar `docs/`:**

```bash
# Actualizar documentación relevante
# Ejemplos según el tipo de tarea:

# Si es modelo/API:
# - docs/api/[endpoint].md
# - docs/architecture/database-schema.md

# Si es componente:
# - docs/architecture/frontend-architecture.md
# - docs/guides/component-library.md

# Si es feature completa:
# - docs/guides/user-guide.md
# - README.md (si aplica)

# SIEMPRE:
# - CHANGELOG.md (obligatorio)
# - docs/sprints/sprint-N/progress.md (tracking del sprint)
```

**Ejemplo de commit de documentación:**
```bash
git add docs/api/products.md CHANGELOG.md
git commit -m "docs(products): update API documentation for barcode search"
```

### Paso 6: Pull Request

Crear PR solo después de actualizar documentación.

### Paso 7: Code Review → Merge → Siguiente Tarea

```bash
# Después de aprobación y merge
git checkout dev
git pull origin dev
git branch -d feature/sprint1-001-product-model

# Siguiente tarea
git checkout -b feature/sprint1-002-product-search-api
```

---

## 🏷️ Nomenclatura de Ramas

### Formato ESTRICTO

```
<tipo>/<sprint>-<numero>-<descripcion-corta>
```

### Ejemplos:

```bash
# Features
feature/sprint1-001-product-model
feature/sprint1-002-sale-api
feature/sprint2-015-payment-methods

# Bugfixes (detectados en sprint)
bugfix/sprint1-fix-barcode-validation
bugfix/sprint2-fix-total-calculation

# Hotfixes (producción)
hotfix/v1.0.1-critical-sale-bug
```

---

## 📊 Estimación de Tareas

### Story Points (Fibonacci)

| Points | Complejidad      | Tiempo Estimado | Descripción             |
| ------ | ---------------- | --------------- | ----------------------- |
| 1      | Trivial          | < 2 horas       | Cambio muy simple       |
| 2      | Simple           | 2-4 horas       | Tarea clara y directa   |
| 3      | Moderada         | 4-8 horas       | Requiere algo de diseño |
| 5      | Compleja         | 1-2 días        | Tarea significativa     |
| 8      | Muy Compleja     | 2-3 días        | Feature completa        |
| 13     | Épica            | 3-5 días        | Dividir en subtareas    |
| 21+    | Demasiado grande | > 1 semana      | DEBE dividirse          |

### Reglas:

- Una tarea NO debe ser mayor a 8 story points
- Un sprint debe tener entre 20-40 story points total
- Si es mayor a 8, dividir en subtareas

---

## 📈 Métricas de Sprint

### Velocity (Velocidad)

```
Velocity = Story Points Completados / Sprint
```

**Ejemplo:**

- Sprint 1: 25 puntos completados
- Sprint 2: 30 puntos completados
- Sprint 3: 28 puntos completados
- **Velocity promedio: 27-28 puntos**

Usar para planificar siguiente sprint.

### Burndown Chart

```
Story Points
    40 │ ╲
    35 │  ╲
    30 │   ╲╲
    25 │    ╲╲
    20 │      ╲╲
    15 │       ╲╲
    10 │         ╲╲
     5 │          ╲╲
     0 │___________╲╲
       1  3  5  7  9 11 13  Días
```

Tracking diario del progreso.

---

## 📝 Definition of Done (DoD)

### Una tarea está DONE cuando:

**Código:**

- [ ] Código implementado y funcional
- [ ] Sigue estándares del proyecto (.cursorrules)
- [ ] Funciones documentadas (docstrings/JSDoc)
- [ ] Sin warnings de linter
- [ ] Sin console.log() o print()

**Testing:**

- [ ] Tests unitarios escritos
- [ ] Tests pasan (coverage >80%)
- [ ] Testing manual realizado
- [ ] Sin bugs conocidos

**Documentación:**

- [ ] CHANGELOG.md actualizado
- [ ] Documentación de API actualizada (si aplica)
- [ ] README actualizado (si aplica)
- [ ] Comentarios útiles en código complejo

**Control de Versiones:**

- [ ] Commits siguen Conventional Commits
- [ ] PR creado hacia `dev`
- [ ] Code review aprobado
- [ ] CI/CD pasa (cuando se implemente)

**Integración:**

- [ ] Merge a `dev` exitoso
- [ ] Sin conflictos
- [ ] Rama eliminada
- [ ] Issue cerrado

---

## 🎯 Priorización de Tareas

### Método MoSCoW

**Must Have (Debe tener)** 🔴

- Funcionalidad crítica
- Sin esto, el sistema no funciona
- **Prioridad: Alta**

**Should Have (Debería tener)** 🟡

- Importante pero no crítico
- Se puede posponer si es necesario
- **Prioridad: Media**

**Could Have (Podría tener)** 🟢

- Nice to have
- Mejora la experiencia
- **Prioridad: Baja**

**Won't Have (No tendrá)** ⚪

- Fuera de scope actual
- Para versiones futuras
- **Backlog futuro**

---

## 📋 Plantillas de Documentación

### Sprint Planning

**Archivo:** `docs/sprints/sprint-N/planning.md`

```markdown
# Sprint N - [Nombre Descriptivo]

**Fecha Inicio:** DD/MM/YYYY
**Fecha Fin:** DD/MM/YYYY
**Duración:** 2 semanas
**Velocity Objetivo:** XX story points

## 🎯 Objetivo del Sprint

[Descripción clara de qué se quiere lograr]

## 📋 User Stories Seleccionadas

### US-XXX: [Título]

- **Story Points:** X
- **Prioridad:** Alta/Media/Baja
- **Asignado a:** @usuario

[Repetir para cada US]

## 📊 Métricas

- **Total Story Points:** XX
- **Tareas Totales:** XX
- **Velocity Anterior:** XX

## 👥 Team

- **Product Owner:** [Nombre]
- **Scrum Master:** [Nombre]
- **Developers:** [Lista]

## 🎯 Definition of Done

[Criterios específicos para este sprint]
```

### Sprint Retrospective

**Archivo:** `docs/sprints/sprint-N/retrospective.md`

```markdown
# Sprint N - Retrospectiva

**Fecha:** DD/MM/YYYY
**Participantes:** [Lista]

## 📊 Métricas Finales

- **Story Points Planificados:** XX
- **Story Points Completados:** XX (XX%)
- **Velocity Real:** XX
- **Tareas Completadas:** XX/XX

## ✅ Qué funcionó bien

1. [Item 1]
2. [Item 2]

## ❌ Qué no funcionó

1. [Item 1]
2. [Item 2]

## 💡 Ideas de mejora

1. [Idea 1]
2. [Idea 2]

## 🎯 Acciones para el siguiente sprint

- [ ] Acción concreta 1 (Responsable: @usuario)
- [ ] Acción concreta 2 (Responsable: @usuario)

## 🎉 Logros destacados

- [Logro 1]
- [Logro 2]

## 🚧 Impedimentos

- [Impedimento 1] - Status: Resuelto/Pendiente
- [Impedimento 2] - Status: Resuelto/Pendiente
```

---

## 🚀 Flujo Completo de Trabajo

```
1. PLANNING
   ├─ Crear docs/sprints/sprint-N/planning.md
   ├─ Crear docs/sprints/sprint-N/user-stories.md
   └─ Crear GitHub Issues

2. DESARROLLO (por cada tarea)
   ├─ git checkout -b feature/sprint1-XXX-descripcion
   ├─ Desarrollar
   ├─ Commits frecuentes
   ├─ Tests
   ├─ Actualizar CHANGELOG.md (obligatorio)
   ├─ Actualizar docs/ relevante (obligatorio)
   ├─ Commit de documentación
   ├─ Push
   └─ Crear Pull Request

3. CODE REVIEW
   ├─ Revisor asignado
   ├─ Comentarios y cambios
   ├─ Aprobación
   └─ Merge a dev

4. CLOSURE
   ├─ Eliminar rama
   ├─ Cerrar issue
   └─ Siguiente tarea

5. SPRINT REVIEW (día 13-14)
   ├─ Demo de features
   ├─ Feedback
   └─ Acceptance

6. RETROSPECTIVE (día 14)
   ├─ Análisis del sprint
   ├─ Documentar aprendizajes
   └─ Planificar mejoras

7. RELEASE (si aplica)
   ├─ Crear rama release/vX.X.0
   ├─ Merge a main
   ├─ Tag versión
   ├─ Merge a dev
   └─ Deploy
```

---

## ⚠️ Reglas ESTRICTAS

### ❌ NUNCA hacer:

1. Trabajar directamente en `dev` o `main`
2. Hacer PR directo a `main` (solo release/hotfix)
3. Merge sin code review
4. Commits sin seguir Conventional Commits
5. Tareas sin issue de GitHub asociado
6. Saltar el Definition of Done
7. Agregar features no planificadas en el sprint
8. Dejar ramas sin eliminar después de merge

### ✅ SIEMPRE hacer:

1. Una tarea = Una rama = Un PR
2. Commits frecuentes y descriptivos
3. Tests antes del PR
4. **Actualizar CHANGELOG.md (OBLIGATORIO)**
5. **Actualizar docs/ relevante (OBLIGATORIO)**
6. Commit específico para documentación
7. Documentar decisiones importantes
8. Daily standup (aunque sea async)
9. Revisar PRs en < 24 horas
10. Cerrar issues al completar

---

## 📞 Comunicación

### Canales:

- **GitHub Issues:** Tareas y bugs
- **Pull Requests:** Code review y discusión técnica
- **docs/sprints/:** Documentación oficial
- **CHANGELOG.md:** Historial de cambios
- **Stand-ups:** Actualizaciones diarias

### Formato de Standup (async si es necesario):

```markdown
**Ayer:**

- Completé T-005 (API de búsqueda)
- Empecé T-006 (Componente Scanner)

**Hoy:**

- Terminar T-006
- Empezar T-007 (ProductList)

**Impedimentos:**

- Ninguno / [Descripción si hay]
```

---

**Última actualización:** 2025-01-XX
**Versión:** 1.0.0
**Mantenedores:** @gastonfr24
````
