# Guía del Formato de Sprints

**Obligatorio para TODO el equipo de desarrollo**

---

## 🎯 Regla Fundamental

> **TODO el trabajo DEBE estar documentado en un sprint activo.**  
> **NUNCA trabajar sin sprint planificado.**  
> **NUNCA hacer cambios que no estén en un sprint.**

---

## 📁 Estructura Obligatoria de Sprint

Cada sprint DEBE tener su carpeta en `docs/sprints/sprint-N/`:

```
docs/sprints/
├── README.md                    # Índice de todos los sprints
└── sprint-N/
    ├── planning.md              # Planificación del sprint
    ├── user-stories.md          # User stories con tareas detalladas
    ├── progress.md              # Seguimiento diario
    └── retrospective.md         # Retrospectiva final
```

---

## 📄 Contenido de Cada Archivo

### 1. planning.md

**Propósito:** Definir el objetivo, alcance y organización del sprint.

**Secciones obligatorias:**

```markdown
# Sprint N - [NOMBRE DESCRIPTIVO]

**Fecha Inicio:** DD/MM/YYYY
**Fecha Fin:** DD/MM/YYYY
**Duración:** 2 semanas
**Velocity Objetivo:** XX story points

## 🎯 Objetivo del Sprint
[Descripción clara del objetivo principal]

## 📋 User Stories Seleccionadas
- US-XXX: [Título] - X story points - Prioridad
- US-XXX: [Título] - X story points - Prioridad

## 📊 Métricas
- Total Story Points: XX
- Tareas Totales: XX
- Velocity Objetivo: XX

## 👥 Team
- Product Owner: [nombre]
- Scrum Master: [nombre]
- Developers: [nombres]

## 🎯 Definition of Done
- [ ] Criterio 1
- [ ] Criterio 2

## 🏗️ Arquitectura Técnica
[Descripción de la arquitectura que se implementará]

## 📅 Planning Detallado
[Desglose por semanas]

## 🚧 Impedimentos Potenciales
[Riesgos identificados]

## 🎯 Criterios de Éxito del Sprint
[Qué debe cumplirse para considerar el sprint exitoso]
```

---

### 2. user-stories.md (ARCHIVO MÁS IMPORTANTE)

**Propósito:** Documentar TODAS las tareas del sprint con checkboxes.

**Formato OBLIGATORIO:**

```markdown
# Sprint N - User Stories Detalladas

---

## US-XXX: [Título de la User Story]

**Como** [rol]
**Quiero** [funcionalidad]
**Para** [beneficio]

**Story Points:** X
**Prioridad:** 🔴 Alta / 🟡 Media / 🟢 Baja

### Criterios de Aceptación:

- [ ] Criterio 1
- [ ] Criterio 2
- [ ] Criterio 3

### Tareas Técnicas:

**Backend:**

- [ ] **T-001:** [Descripción de la tarea]
  - Detalle 1
  - Detalle 2
  - Tests requeridos
  - **Rama:** `feature/sprint1-001-descripcion-corta`
  - **Estimado:** X horas

- [ ] **T-002:** [Descripción de la tarea]
  - Detalle 1
  - **Rama:** `feature/sprint1-002-descripcion-corta`
  - **Estimado:** X horas

**Frontend:**

- [ ] **T-003:** [Descripción de la tarea]
  - Detalle 1
  - **Rama:** `feature/sprint1-003-descripcion-corta`
  - **Estimado:** X horas

---

## 📊 Resumen de Tareas

| Tarea | Tipo | US | Estimado | Asignado |
|-------|------|-----|----------|----------|
| T-001 | Backend | US-XXX | Xh | @usuario |
| T-002 | Backend | US-XXX | Xh | @usuario |
| T-003 | Frontend | US-XXX | Xh | @usuario |
| **TOTAL** | - | - | **XXh** | - |
```

#### ✅ Reglas de Checkboxes en user-stories.md:

1. **Iniciar sprint:**
   - TODAS las tareas con `[ ]` (sin marcar)

2. **Durante el sprint:**
   - NO marcar en este archivo
   - Solo se marca en `progress.md`

3. **Al completar tarea:**
   - Cambiar `[ ]` a `[x]` cuando la tarea está 100% completada
   - Esto incluye: código + tests + docs + PR merged

4. **Formato estricto:**
   ```markdown
   - [ ] **T-001:** Descripción  # Pendiente
   - [x] **T-002:** Descripción  # Completada
   ```

---

### 3. progress.md (ACTUALIZACIÓN DIARIA OBLIGATORIA)

**Propósito:** Tracking diario del avance del sprint.

**Formato OBLIGATORIO:**

```markdown
# Sprint N - Progress Tracking

**Última actualización:** DD/MM/YYYY

---

## 📊 Estado General

**Progreso:** X/XX tareas completadas (X%)
**Story Points:** X/XX completados (X%)
**Tiempo estimado restante:** XX horas

---

## 📅 Daily Progress

### Lunes DD/MM/YYYY - Día X

**Completado:**
- ✅ T-001: Product model - Completado
- ✅ T-002: Products list API - Completado

**En Progreso:**
- 🟡 T-003: Product search API

**Blockers:**
- Ninguno / [Descripción del blocker]

**Notas:**
- Nota del día

---

### Martes DD/MM/YYYY - Día X

[Mismo formato]

---

## ✅ Tareas Completadas

- [x] T-001: Product model - Completado DD/MM/YYYY
- [x] T-002: Products list API - Completado DD/MM/YYYY

---

## 🟡 Tareas En Progreso

- [ ] T-003: Product search API (Iniciado DD/MM)

---

## ⏳ Tareas Pendientes

### US-XXX: [Título]
- [ ] T-004: [Descripción]
- [ ] T-005: [Descripción]

### US-XXX: [Título]
- [ ] T-006: [Descripción]

---

## 📈 Burndown

| Día | Fecha | Tareas Restantes | Story Points Restantes |
|-----|-------|------------------|------------------------|
| 1   | DD/MM | XX               | XX                     |
| 2   | DD/MM | XX               | XX                     |
| ... | ...   | ...              | ...                    |
| 14  | DD/MM | 0 (objetivo)     | 0 (objetivo)           |

---

## 🚨 Blockers e Impedimentos

_Lista de impedimentos actuales_

---

## 📝 Notas del Sprint

_Notas generales del sprint_
```

#### ✅ Reglas de Checkboxes en progress.md:

1. **Al iniciar una tarea:**
   - Mover de "Pendientes" a "En Progreso"
   - Agregar fecha de inicio
   - Marcar con emoji 🟡

2. **Al completar una tarea:**
   - Cambiar `[ ]` a `[x]`
   - Mover de "En Progreso" a "Completadas"
   - Agregar fecha de completado
   - Actualizar "Estado General"
   - Actualizar tabla de Burndown

3. **Actualización diaria:**
   - TODOS LOS DÍAS agregar nueva entrada en "Daily Progress"
   - Actualizar estado de tareas
   - Documentar blockers

---

### 4. retrospective.md

**Propósito:** Documentar aprendizajes al finalizar el sprint.

**Formato OBLIGATORIO:**

```markdown
# Sprint N - Retrospectiva

**Fecha:** DD/MM/YYYY
**Participantes:** [lista]

---

## 📊 Métricas Finales

- **Story Points Planificados:** XX
- **Story Points Completados:** XX
- **Velocity Real:** XX
- **Tareas Completadas:** XX/XX

---

## ✅ Qué funcionó bien

- Elemento 1
- Elemento 2

---

## ❌ Qué no funcionó

- Elemento 1
- Elemento 2

---

## 💡 Ideas de mejora

- Idea 1
- Idea 2

---

## 🎯 Acciones para el siguiente sprint

- [ ] Acción 1
- [ ] Acción 2

---

## 🎉 Logros destacados

- Logro 1
- Logro 2

---

## 🚧 Impedimentos

- Impedimento 1 (estado)
- Impedimento 2 (estado)
```

---

## 🔄 Proceso Completo de Sprint

### Fase 1: Planning (Día 1)

**Pasos:**

1. Crear carpeta `docs/sprints/sprint-N/`
2. Crear `planning.md` con objetivo y user stories
3. Crear `user-stories.md` con TODAS las tareas
4. Cada tarea DEBE tener:
   - [ ] ID único (T-001, T-002, etc.)
   - [ ] Descripción clara
   - [ ] Rama de Git especificada
   - [ ] Estimación en horas
   - [ ] Checkbox `[ ]` al inicio
5. Crear `progress.md` con estado inicial
6. Crear `retrospective.md` vacío

✅ **Checklist de Planning:**
- [ ] Carpeta sprint-N creada
- [ ] planning.md completo
- [ ] user-stories.md con todas las tareas
- [ ] Cada tarea tiene ID, rama, estimación
- [ ] progress.md inicializado
- [ ] retrospective.md creado
- [ ] CHANGELOG.md actualizado

---

### Fase 2: Development (Días 2-12)

**Pasos diarios:**

1. **Al INICIAR el día:**
   - Leer `progress.md`
   - Identificar próxima tarea
   - Verificar que está en `user-stories.md`

2. **Al INICIAR una tarea:**
   - Crear rama según `user-stories.md`
   - Actualizar `progress.md`:
     - Mover tarea a "En Progreso"
     - Agregar fecha de inicio
     - Marcar con 🟡

3. **Durante el trabajo:**
   - Hacer commits con Conventional Commits
   - Referenciar tarea en commits: `feat(scope): description [T-001]`

4. **Al COMPLETAR una tarea:**
   - [ ] Código implementado
   - [ ] Tests escritos y pasando
   - [ ] Documentación actualizada
   - [ ] CHANGELOG.md actualizado
   - [ ] `user-stories.md`: Cambiar `[ ]` a `[x]`
   - [ ] `progress.md`: Mover a "Completadas" con fecha
   - [ ] `progress.md`: Actualizar "Estado General"
   - [ ] `progress.md`: Actualizar tabla Burndown
   - [ ] Pull Request creado (referencia T-XXX)

5. **Al FINALIZAR el día:**
   - Actualizar `progress.md` con entrada diaria
   - Documentar lo completado
   - Documentar lo en progreso
   - Documentar blockers
   - Commit: `docs(sprint): update progress day X`

✅ **Checklist por Tarea:**
- [ ] Tarea está en user-stories.md
- [ ] Rama creada según especificación
- [ ] Código implementado
- [ ] Tests pasando
- [ ] Docs actualizadas
- [ ] CHANGELOG.md actualizado
- [ ] user-stories.md: checkbox marcado [x]
- [ ] progress.md: tarea en "Completadas"
- [ ] progress.md: estado general actualizado
- [ ] PR creado con referencia a tarea

---

### Fase 3: Testing & Refinement (Días 11-13)

**Pasos:**

1. Testing completo del sprint
2. Corrección de bugs
3. Refinamiento de UX
4. Documentación final
5. Actualizar `progress.md` diariamente

---

### Fase 4: Review & Retrospective (Día 14)

**Pasos:**

1. **Sprint Review:**
   - Demo de funcionalidades
   - Validar Definition of Done
   - Documentar resultados

2. **Sprint Retrospective:**
   - Completar `retrospective.md`
   - Documentar métricas finales
   - Identificar mejoras

3. **Cierre del Sprint:**
   - Verificar que TODAS las tareas tienen checkbox marcado
   - Actualizar README.md de sprints
   - Actualizar CHANGELOG.md con release
   - Tag de versión si aplica
   - Commit: `docs(sprint): complete sprint N retrospective`

✅ **Checklist de Cierre:**
- [ ] Todas las tareas completadas o justificadas
- [ ] Todos los checkboxes marcados
- [ ] progress.md finalizado
- [ ] retrospective.md completado
- [ ] CHANGELOG.md actualizado
- [ ] README de sprints actualizado
- [ ] Demo realizada
- [ ] Tag de versión (si aplica)

---

## 🚨 Situaciones Especiales

### Si Surge una Tarea Nueva Durante el Sprint

**NO EMPEZAR SIN DOCUMENTAR**

**Opción A - Es urgente y hay capacidad:**

1. Agregar tarea a `user-stories.md`:
   ```markdown
   - [ ] **T-XXX:** [Nueva tarea]
     - **Rama:** `feature/sprintN-XXX-descripcion`
     - **Estimado:** X horas
     - **NOTA:** Agregada durante el sprint (DD/MM)
   ```

2. Agregar a `progress.md` en "Pendientes"
3. Actualizar "Total de Tareas" en ambos archivos
4. Agregar nota en "Daily Progress" explicando por qué se agregó
5. Recién entonces empezar a trabajar

**Opción B - No es urgente:**

1. Agregar al backlog del próximo sprint
2. Documentar en planning.md del próximo sprint

**Opción C - Es un hotfix crítico:**

1. Usar proceso de hotfix (ver .cursorrules)
2. Documentar en CHANGELOG.md
3. NO agregar al sprint actual

---

### Si NO Hay Sprint Activo

**NUNCA trabajar sin sprint.**

1. Planificar nuevo sprint
2. Crear estructura completa
3. Documentar al menos las primeras tareas
4. Recién entonces empezar

---

### Si una Tarea es más Grande de lo Estimado

1. Documentar en `progress.md` - "Notas del día"
2. Si es necesario, partir en sub-tareas
3. Actualizar `user-stories.md` con sub-tareas
4. Marcar como completada solo cuando TODO esté hecho

---

## 📋 Templates Rápidos

### Template de Tarea en user-stories.md

```markdown
- [ ] **T-XXX:** [Título de la tarea]
  - Descripción detallada
  - Criterio de éxito 1
  - Criterio de éxito 2
  - Tests requeridos: [descripción]
  - **Rama:** `feature/sprintN-XXX-descripcion-corta`
  - **Estimado:** X horas
```

### Template de Daily Progress

```markdown
### [Día] DD/MM/YYYY - Día X

**Completado:**
- ✅ T-XXX: [Descripción] - Completado

**En Progreso:**
- 🟡 T-XXX: [Descripción]

**Blockers:**
- Ninguno

**Notas:**
- [Notas del día]
```

### Template de Commit de Documentación

```bash
# Al completar tarea
git commit -m "docs(sprint): mark T-XXX as completed"

# Al finalizar el día
git commit -m "docs(sprint): update progress day X"

# Al cerrar sprint
git commit -m "docs(sprint): complete sprint N retrospective"
```

---

## ✅ Checklist para Cursor AI

**ANTES de hacer cualquier trabajo:**

- [ ] Verificar que existe sprint activo en `docs/sprints/sprint-N/`
- [ ] Leer `user-stories.md` para encontrar la tarea
- [ ] Verificar que la tarea tiene ID, rama, y estimación
- [ ] Si NO existe → Preguntar al usuario y documentar primero

**DURANTE el trabajo:**

- [ ] Crear rama según especificación en `user-stories.md`
- [ ] Hacer commits con referencia a tarea [T-XXX]
- [ ] Actualizar `progress.md` si cambió algo significativo

**AL COMPLETAR tarea:**

- [ ] Marcar checkbox `[x]` en `user-stories.md`
- [ ] Mover tarea a "Completadas" en `progress.md`
- [ ] Agregar fecha de completado
- [ ] Actualizar "Estado General" en `progress.md`
- [ ] Actualizar tabla Burndown
- [ ] Actualizar CHANGELOG.md
- [ ] Actualizar `docs/` según corresponda
- [ ] Crear PR con referencia a tarea

**NUNCA:**

- ❌ Trabajar sin verificar sprint activo
- ❌ Empezar tarea que no está en user-stories.md
- ❌ Olvidar marcar checkboxes
- ❌ Olvidar actualizar progress.md
- ❌ Crear rama sin seguir nomenclatura

---

## 📚 Referencias

- Ver `.cursorrules` para reglas completas
- Ver `docs/methodology/sprint-workflow.md` para proceso detallado
- Ver `docs/methodology/documentation-update-guide.md` para docs
- Ver ejemplos en `docs/sprints/sprint-1/`

---

**Última actualización:** 27/01/2025  
**Mantenido por:** @gastonfr24  
**Estado:** ✅ Obligatorio para todo el equipo

