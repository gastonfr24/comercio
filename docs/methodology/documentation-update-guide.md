# 📝 Guía de Actualización de Documentación por Tarea

## 🎯 Regla Principal

**AL FINALIZAR CADA TAREA, ACTUALIZAR `docs/` ES OBLIGATORIO**

Esta no es una sugerencia, es un requisito para que el PR sea aprobado.

---

## 📋 Qué Documentar Según el Tipo de Tarea

### Backend - Modelos de Datos

**Archivos a actualizar:**
- `docs/architecture/database-schema.md`
- `CHANGELOG.md`

**Ejemplo:**
```markdown
## Modelo Product

**Tabla:** products

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | UUID | Identificador único |
| barcode | VARCHAR(50) | Código de barras |
| name | VARCHAR(200) | Nombre del producto |
| price | DECIMAL(10,2) | Precio de venta |
| cost | DECIMAL(10,2) | Costo de compra |
| stock | INTEGER | Cantidad en stock |
| created_at | TIMESTAMP | Fecha de creación |
```

### Backend - API Endpoints

**Archivos a actualizar:**
- `docs/api/[recurso].md`
- `docs/architecture/api-design.md`
- `CHANGELOG.md`

**Ejemplo:**
```markdown
## GET /api/products/search/

Busca productos por código de barras.

**Query Parameters:**
- `barcode` (string, required): Código de barras a buscar

**Response 200:**
```json
{
  "id": "uuid",
  "barcode": "7501234567890",
  "name": "Coca-Cola 500ml",
  "price": 25.00,
  "stock": 45
}
```

**Errores:**
- 404: Product not found
- 400: Invalid barcode format
```

### Frontend - Componentes

**Archivos a actualizar:**
- `docs/architecture/frontend-architecture.md`
- `docs/guides/component-library.md` (si aplica)
- `CHANGELOG.md`

**Ejemplo:**
```markdown
## ScannerInput Component

**Ubicación:** `src/components/pos/ScannerInput.tsx`

**Propósito:** Captura input del escáner de códigos de barras.

**Props:**
```typescript
interface ScannerInputProps {
  onScan: (barcode: string) => void
  placeholder?: string
  autoFocus?: boolean
}
```

**Uso:**
```tsx
<ScannerInput 
  onScan={handleProductScan}
  autoFocus
/>
```

**Características:**
- Auto-focus en mount
- Detecta enter para enviar
- Limpia input después de scan
```

### Features Completas

**Archivos a actualizar:**
- `docs/guides/user-guide.md`
- `docs/architecture/overview.md`
- `README.md` (si afecta instalación/setup)
- `CHANGELOG.md`

**Ejemplo:**
```markdown
## Sistema de Ventas

El módulo de ventas permite registrar transacciones de forma rápida.

### Cómo Usar:

1. Ir a "Nueva Venta"
2. Escanear productos o buscar por nombre
3. Revisar total
4. Seleccionar método de pago
5. Confirmar venta
6. Imprimir ticket

### Atajos de Teclado:

- `F2`: Nueva venta
- `F9`: Cobrar
- `ESC`: Cancelar
```

### Tests

**Archivos a actualizar:**
- `docs/guides/testing.md`
- `CHANGELOG.md`

**Ejemplo:**
```markdown
## Tests del Módulo Products

**Backend:**
```bash
pytest apps/products/tests/
```

**Coverage:** 95%

**Tests Importantes:**
- `test_product_creation`: Creación de productos
- `test_barcode_validation`: Validación de código de barras
- `test_stock_update`: Actualización de stock
```

---

## 📁 Estructura de docs/ y Cuándo Actualizar

```
docs/
├── README.md                          # Actualizar: Nuevas secciones grandes
├── CHANGELOG.md                       # Actualizar: SIEMPRE (cada tarea)
│
├── architecture/                      # Actualizar: Cambios estructurales
│   ├── overview.md                   # → Nuevas features importantes
│   ├── backend-architecture.md       # → Modelos, servicios, APIs
│   ├── frontend-architecture.md      # → Componentes, routing, estado
│   ├── database-schema.md            # → Modelos nuevos/modificados
│   └── api-design.md                 # → Endpoints nuevos/modificados
│
├── api/                              # Actualizar: Endpoints nuevos/modificados
│   ├── README.md                     # → Índice de endpoints
│   ├── authentication.md             # → APIs de auth
│   ├── products.md                   # → APIs de productos
│   ├── sales.md                      # → APIs de ventas
│   └── cash-register.md              # → APIs de caja
│
├── guides/                           # Actualizar: Features de usuario
│   ├── getting-started.md           # → Setup inicial
│   ├── user-guide.md                # → Uso del sistema
│   ├── component-library.md         # → Componentes UI
│   ├── testing.md                   # → Tests nuevos
│   └── troubleshooting.md           # → Problemas comunes
│
├── sprints/                          # Actualizar: Progreso del sprint
│   └── sprint-N/
│       ├── planning.md              # → Al inicio del sprint
│       ├── user-stories.md          # → Al inicio del sprint
│       ├── progress.md              # → CADA TAREA completada
│       └── retrospective.md         # → Al final del sprint
│
├── project/                          # Actualizar: Cambios en reqs
│   ├── kiosko-requirements.md       # → Cambios en requisitos
│   └── kiosko-sprint-plan.md        # → Ajustes al plan
│
└── methodology/                      # Actualizar: Mejoras de proceso
    ├── sprint-workflow.md           # → Cambios en metodología
    └── documentation-update-guide.md # → Este archivo
```

---

## ✅ Checklist por Tarea

### Antes de crear el Pull Request:

**1. Código:**
- [ ] Feature implementada
- [ ] Tests escritos
- [ ] Tests pasando

**2. Documentación en Código:**
- [ ] Docstrings/JSDoc agregados
- [ ] Comentarios útiles (si necesario)
- [ ] Type hints/interfaces

**3. CHANGELOG.md (OBLIGATORIO):**
- [ ] Entrada agregada en [Unreleased]
- [ ] Categoría correcta (Added/Changed/Fixed)
- [ ] Formato: `tipo(scope): descripción`

**4. docs/ (OBLIGATORIO según tipo):**
- [ ] Architecture docs actualizados (si aplica)
- [ ] API docs actualizados (si aplica)
- [ ] User guides actualizados (si aplica)
- [ ] Component docs actualizados (si aplica)
- [ ] `docs/sprints/sprint-N/progress.md` actualizado

**5. Commit de Documentación:**
```bash
git add docs/ CHANGELOG.md
git commit -m "docs(products): update API and architecture documentation"
```

**6. Crear Pull Request:**
- [ ] PR incluye cambios de documentación
- [ ] PR description menciona docs actualizados

---

## 📝 Plantilla de Commit de Documentación

```bash
# Para documentación de API
git commit -m "docs(api): add products search endpoint documentation"

# Para documentación de arquitectura
git commit -m "docs(architecture): update database schema with Product model"

# Para guías de usuario
git commit -m "docs(guides): add sales process to user guide"

# Para múltiples docs
git commit -m "docs(products): update API, architecture and user guide"
```

---

## 🚫 Errores Comunes a Evitar

### ❌ NO HACER:

1. **Crear PR sin actualizar docs**
   ```
   ❌ PR solo con código
   ✅ PR con código + documentación
   ```

2. **"Lo documento después"**
   ```
   ❌ Dejar documentación para después
   ✅ Documentar antes de crear PR
   ```

3. **Documentación vaga**
   ```
   ❌ "Se agregó endpoint de productos"
   ✅ Documentar parámetros, respuestas, ejemplos
   ```

4. **Solo actualizar CHANGELOG**
   ```
   ❌ Solo CHANGELOG.md
   ✅ CHANGELOG.md + docs/ relevantes
   ```

5. **Olvidar progress.md del sprint**
   ```
   ❌ No actualizar progreso del sprint
   ✅ Marcar tarea completada en progress.md
   ```

---

## 📊 Ejemplo Completo de Flujo con Documentación

### Tarea: Implementar búsqueda de productos por código de barras

**1. Desarrollo:**
```bash
git checkout -b feature/sprint1-002-product-search-api

# Implementar código
# Escribir tests
```

**2. Documentación:**
```bash
# Actualizar API docs
vim docs/api/products.md
# Agregar:
# - Endpoint GET /api/products/search/
# - Parámetros
# - Respuestas
# - Ejemplos

# Actualizar architecture
vim docs/architecture/api-design.md
# Agregar referencia al nuevo endpoint

# Actualizar CHANGELOG
vim CHANGELOG.md
# Agregar: feat(products): add barcode search endpoint

# Actualizar progreso del sprint
vim docs/sprints/sprint-1/progress.md
# Marcar T-002 como completada
```

**3. Commit de documentación:**
```bash
git add docs/api/products.md
git add docs/architecture/api-design.md
git add docs/sprints/sprint-1/progress.md
git add CHANGELOG.md
git commit -m "docs(products): add barcode search API documentation"
```

**4. Push y PR:**
```bash
git push origin feature/sprint1-002-product-search-api
# Crear PR que incluye código + documentación
```

---

## 🎯 Beneficios de Documentar Cada Tarea

1. **Documentación siempre actualizada**
   - No se acumula "deuda de documentación"
   - Refleja el estado actual del código

2. **Onboarding más fácil**
   - Nuevos desarrolladores encuentran info actualizada
   - Menos preguntas, más autonomía

3. **Mejor code review**
   - Reviewer entiende el cambio con contexto
   - Documentación se revisa junto con código

4. **Tracking del sprint**
   - progress.md muestra estado real
   - Fácil ver qué falta

5. **Menos bugs**
   - Documentar obliga a pensar en edge cases
   - APIs mejor definidas

---

## 📞 ¿Qué hacer si no sé qué documentar?

### Preguntas guía:

1. **¿Agregaste un endpoint?** → Documenta en `docs/api/`
2. **¿Creaste un modelo?** → Actualiza `docs/architecture/database-schema.md`
3. **¿Nuevo componente?** → Documenta en `docs/architecture/frontend-architecture.md`
4. **¿Feature de usuario?** → Actualiza `docs/guides/user-guide.md`
5. **¿Cambio estructural?** → Actualiza `docs/architecture/overview.md`

### Si aún tienes dudas:

- Mira tareas similares anteriores
- Pregunta en el PR
- Consulta `DOCUMENTATION_GUIDE.md`
- **En duda, documenta más que menos**

---

## ⚠️ Consecuencias de No Documentar

### El PR será RECHAZADO si:

- ❌ No se actualizó CHANGELOG.md
- ❌ No se actualizó docs/ correspondiente
- ❌ No se actualizó progress.md del sprint
- ❌ Documentación es vaga o incompleta

### No hay excepciones:
- "Es una tarea pequeña" → Igual se documenta
- "Es solo un fix" → CHANGELOG.md mínimo
- "No tuve tiempo" → Hacer tiempo antes del PR

---

## 📚 Referencias

- `DOCUMENTATION_GUIDE.md` - Guía general de documentación
- `docs/guides/code-documentation-standards.md` - Estándares de código
- `.cursorrules` - Reglas del proyecto
- `docs/methodology/sprint-workflow.md` - Flujo de trabajo

---

**Última actualización:** 2025-01-XX  
**Versión:** 1.0.0  
**Mantenedores:** @gastonfr24

**Recuerda:** La documentación no es opcional, es parte integral del desarrollo profesional.

