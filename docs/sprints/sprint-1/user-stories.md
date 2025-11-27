# Sprint 1 - User Stories Detalladas

---

## US-001: Registro rápido de venta

**Como** cajero del kiosco  
**Quiero** registrar ventas escaneando o buscando productos  
**Para** cobrar de forma rápida y sin errores

**Story Points:** 8  
**Prioridad:** 🔴 Alta

### Criterios de Aceptación:

- [ ] Puedo buscar productos por código de barras
- [ ] Puedo buscar productos por nombre
- [ ] Se muestra el producto con su precio
- [ ] Se agrega al carrito visible
- [ ] Se acumula el total automáticamente
- [ ] Puedo modificar cantidad de un item
- [ ] Puedo eliminar un item si me equivoqué
- [ ] El proceso toma menos de 30 segundos

### Tareas Técnicas:

**Backend:**

- [x] **T-001:** Crear app `products` y modelo Product ✅ COMPLETADA

  - ✅ Campos: barcode, name, price, cost, stock, category, is_active
  - ✅ Validaciones de barcode
  - ✅ Tests del modelo (16 tests pasando)
  - ✅ Cambiar python-decouple por django-environ
  - ✅ Configurar archivos .env (backend y frontend)
  - ✅ Configurar .env.dev para Docker
  - ✅ Actualizar docker-compose.dev.yml para usar archivos .env
  - ✅ Django admin configurado
  - ✅ Migraciones creadas y aplicadas
  - **Rama:** `feature/sprint1-001-product-model`
  - **Estimado:** 4 horas | **Real:** 4 horas

- [x] **T-002:** API endpoint GET /api/products/ ✅ COMPLETADA

  - ✅ Listar productos activos (por defecto)
  - ✅ Filtros: search, category, is_active
  - ✅ Paginación (20 items por página, customizable)
  - ✅ Ordenamiento por múltiples campos
  - ✅ Serializers: ProductSerializer y ProductListSerializer
  - ✅ ViewSet con operaciones CRUD completas
  - ✅ Tests de API (17 tests pasando)
  - **Rama:** `feature/sprint1-002-products-list-api`
  - **Estimado:** 2 horas | **Real:** 2 horas

- [x] **T-003:** API endpoint GET /api/products/search/ ✅ COMPLETADA

  - ✅ Búsqueda por barcode (exacto, case-insensitive)
  - ✅ Búsqueda por nombre (parcial, case-insensitive)
  - ✅ Prioridad a matches de barcode
  - ✅ Response rápido (< 100ms)
  - ✅ Limita resultados a 10 items
  - ✅ Tests de búsqueda (11 tests pasando)
  - **Rama:** `feature/sprint1-003-product-search-api`
  - **Estimado:** 3 horas | **Real:** 1 hora

- [x] **T-004:** Crear app `sales` con modelos Sale y SaleItem ✅ COMPLETADA

  - ✅ Sale: total, payment_type (cash/card/transfer), date, status (pending/completed/cancelled)
  - ✅ SaleItem: product, quantity, unit_price, subtotal (auto-calculado)
  - ✅ Relaciones FK correctas (Sale ← SaleItem → Product)
  - ✅ Métodos: calculate_total(), complete_sale(), cancel_sale()
  - ✅ Gestión automática de stock
  - ✅ Validaciones completas
  - ✅ Django admin con inline editing
  - ✅ Tests de modelos (24 tests pasando)
  - **Rama:** `feature/sprint1-004-sale-models`
  - **Estimado:** 4 horas | **Real:** 3.5 horas

- [x] **T-005:** API endpoint POST /api/sales/ ✅ COMPLETADA
  - ✅ Crear venta con items
  - ✅ Validar stock disponible
  - ✅ Descontar stock automáticamente
  - ✅ Calcular totales
  - ✅ Cancelación de ventas con restauración de stock
  - ✅ Tests de creación (14 tests de API pasando)
  - **Rama:** `feature/sprint1-004-sale-models` (incluida en PR #4)
  - **Estimado:** 5 horas | **Real:** 3 horas

**Frontend:**

- [ ] **T-006:** Componente ScannerInput

  - Input con autofocus
  - Detecta enter para buscar
  - Loading state
  - Error handling
  - **Rama:** `feature/sprint1-006-scanner-input`
  - **Estimado:** 2 horas

- [ ] **T-007:** Componente ProductList para búsqueda

  - Muestra resultados de búsqueda
  - Click para agregar al carrito
  - Grid responsive
  - **Rama:** `feature/sprint1-007-product-list`
  - **Estimado:** 3 horas

- [ ] **T-008:** Hook useCart para estado del carrito

  - Add item
  - Remove item
  - Update quantity
  - Calculate totals
  - Tests del hook
  - **Rama:** `feature/sprint1-008-use-cart-hook`
  - **Estimado:** 4 horas

- [ ] **T-009:** Componente CartSummary

  - Lista de items en carrito
  - Totales
  - Botones de cantidad
  - Botón eliminar
  - **Rama:** `feature/sprint1-009-cart-summary`
  - **Estimado:** 3 horas

- [ ] **T-010:** Página /pos (Point of Sale)
  - Layout principal
  - Integrar ScannerInput
  - Integrar ProductList
  - Integrar CartSummary
  - **Rama:** `feature/sprint1-010-pos-page`
  - **Estimado:** 3 horas

---

## US-002: Gestión básica de productos

**Como** administrador  
**Quiero** dar de alta, modificar y eliminar productos  
**Para** mantener el catálogo actualizado

**Story Points:** 5  
**Prioridad:** 🔴 Alta

### Criterios de Aceptación:

- [ ] Puedo crear un producto nuevo
- [ ] Puedo editar precio de un producto
- [ ] Puedo editar stock de un producto
- [ ] Puedo desactivar un producto
- [ ] Veo lista de todos los productos
- [ ] El formulario es simple y claro

### Tareas Técnicas:

**Backend:**

- [ ] **T-011:** API endpoint POST /api/products/

  - Crear producto
  - Validaciones
  - Tests
  - **Rama:** `feature/sprint1-011-create-product-api`
  - **Estimado:** 2 horas

- [ ] **T-012:** API endpoints PUT/PATCH /api/products/{id}/
  - Actualizar producto
  - Validaciones
  - Tests
  - **Rama:** `feature/sprint1-012-update-product-api`
  - **Estimado:** 2 horas

**Frontend:**

- [ ] **T-013:** Componente ProductForm

  - Campos: barcode, name, price, cost, stock
  - Validaciones
  - Loading states
  - **Rama:** `feature/sprint1-013-product-form`
  - **Estimado:** 3 horas

- [ ] **T-014:** Componente ProductTable

  - Lista de productos en tabla
  - Botones editar/eliminar
  - Búsqueda en tabla
  - **Rama:** `feature/sprint1-014-product-table`
  - **Estimado:** 3 horas

- [ ] **T-015:** Página /products
  - Layout principal
  - Integrar ProductForm
  - Integrar ProductTable
  - **Rama:** `feature/sprint1-015-products-page`
  - **Estimado:** 2 horas

---

## US-003: Cobro y métodos de pago

**Como** cajero  
**Quiero** cobrar la venta y elegir método de pago  
**Para** completar la transacción

**Story Points:** 8  
**Prioridad:** 🔴 Alta

### Criterios de Aceptación:

- [ ] Puedo ver el total a cobrar claramente
- [ ] Puedo elegir método de pago (efectivo/tarjeta)
- [ ] Si es efectivo, puedo ingresar monto recibido
- [ ] Se calcula el vuelto automáticamente
- [ ] Se confirma la venta
- [ ] Se limpia el carrito después de cobrar
- [ ] Veo confirmación visual de venta exitosa

### Tareas Técnicas:

**Backend:**

- [ ] **T-016:** Agregar campo payment_type a Sale

  - Choices: cash, card, other
  - Migración
  - Tests
  - **Rama:** `feature/sprint1-016-payment-type-field`
  - **Estimado:** 1 hora

- [ ] **T-017:** Endpoint POST /api/sales/confirm/

  - Confirmar venta
  - Actualizar stock
  - Registrar en caja
  - Tests
  - **Rama:** `feature/sprint1-017-confirm-sale-api`
  - **Estimado:** 3 horas

- [ ] **T-017b:** Integración de MercadoPago
  - Instalar mercadopago SDK
  - Crear preference de pago
  - Webhook para notificaciones
  - Endpoint POST /api/payments/mercadopago/create/
  - Endpoint POST /api/payments/mercadopago/webhook/
  - Verificación de pagos
  - Tests de integración
  - **Rama:** `feature/sprint1-017b-mercadopago-integration`
  - **Estimado:** 5 horas

**Frontend:**

- [ ] **T-018:** Componente PaymentModal

  - Modal grande y claro
  - Botones de métodos de pago
  - Input de monto recibido (efectivo)
  - Cálculo de vuelto
  - Confirmación
  - **Rama:** `feature/sprint1-018-payment-modal`
  - **Estimado:** 4 horas

- [ ] **T-019:** Integrar PaymentModal en POS
  - Botón "COBRAR" grande
  - Abrir modal al cobrar
  - Confirmar venta
  - Limpiar carrito
  - Mensaje de éxito
  - **Rama:** `feature/sprint1-019-integrate-payment`
  - **Estimado:** 2 horas

---

## US-004: Apertura/Cierre de caja básico

**Como** cajero  
**Quiero** abrir la caja al inicio y cerrarla al final del día  
**Para** controlar el efectivo

**Story Points:** 5  
**Prioridad:** 🔴 Alta

### Criterios de Aceptación:

- [ ] Puedo abrir caja con monto inicial
- [ ] Se registra fecha/hora de apertura
- [ ] Durante el día puedo ver si hay caja abierta
- [ ] Al cerrar, veo total de ventas del día
- [ ] Puedo ingresar efectivo contado
- [ ] Se muestra diferencia (faltante/sobrante)
- [ ] Se registra fecha/hora de cierre

### Tareas Técnicas:

**Backend:**

- [ ] **T-020:** Crear app `cash_register` y modelo CashRegister

  - Campos: opening_date, closing_date, opening_cash, closing_cash, sales_total, user
  - Status: open, closed
  - Tests
  - **Rama:** `feature/sprint1-020-cash-register-model`
  - **Estimado:** 3 horas

- [ ] **T-021:** API endpoints para caja
  - POST /api/cash-register/open/
  - GET /api/cash-register/current/
  - POST /api/cash-register/close/
  - Tests
  - **Rama:** `feature/sprint1-021-cash-register-api`
  - **Estimado:** 4 horas

**Frontend:**

- [ ] **T-022:** Componente OpenCashForm

  - Input de monto inicial
  - Confirmación
  - **Rama:** `feature/sprint1-022-open-cash-form`
  - **Estimado:** 2 horas

- [ ] **T-023:** Componente CloseCashForm

  - Mostrar total de ventas
  - Input de efectivo contado
  - Calcular diferencia
  - Confirmación
  - **Rama:** `feature/sprint1-023-close-cash-form`
  - **Estimado:** 3 horas

- [ ] **T-024:** Página /cash
  - Estado de caja actual
  - Abrir/Cerrar caja
  - Historial básico
  - **Rama:** `feature/sprint1-024-cash-page`
  - **Estimado:** 2 horas

---

## US-005: Vista de ventas del día

**Como** administrador  
**Quiero** ver un resumen de ventas del día  
**Para** saber cuánto vendí

**Story Points:** 4  
**Prioridad:** 🔴 Alta

### Criterios de Aceptación:

- [ ] Veo total de ventas del día en dinero
- [ ] Veo cantidad de transacciones
- [ ] Veo desglose por método de pago
- [ ] Puedo ver lista de ventas individuales
- [ ] La información es clara y visual

### Tareas Técnicas:

**Backend:**

- [ ] **T-025:** Endpoint GET /api/reports/daily/
  - Ventas del día actual
  - Totales por método de pago
  - Cantidad de transacciones
  - Lista de ventas
  - Tests
  - **Rama:** `feature/sprint1-025-daily-report-api`
  - **Estimado:** 3 horas

**Frontend:**

- [ ] **T-026:** Componente DailySalesReport

  - Cards con métricas
  - Tabla de ventas
  - Diseño visual claro
  - **Rama:** `feature/sprint1-026-daily-sales-report`
  - **Estimado:** 3 horas

- [ ] **T-027:** Página /reports/daily
  - Layout principal
  - Integrar DailySalesReport
  - Actualización en tiempo real
  - **Rama:** `feature/sprint1-027-reports-page`
  - **Estimado:** 2 horas

---

## 📊 Resumen de Tareas

| Tarea     | Tipo     | US     | Estimado | Asignado    |
| --------- | -------- | ------ | -------- | ----------- |
| T-001     | Backend  | US-001 | 3h       | @gastonfr24 |
| T-002     | Backend  | US-001 | 2h       | @gastonfr24 |
| T-003     | Backend  | US-001 | 3h       | @gastonfr24 |
| T-004     | Backend  | US-001 | 4h       | @gastonfr24 |
| T-005     | Backend  | US-001 | 5h       | @gastonfr24 |
| T-006     | Frontend | US-001 | 2h       | @gastonfr24 |
| T-007     | Frontend | US-001 | 3h       | @gastonfr24 |
| T-008     | Frontend | US-001 | 4h       | @gastonfr24 |
| T-009     | Frontend | US-001 | 3h       | @gastonfr24 |
| T-010     | Frontend | US-001 | 3h       | @gastonfr24 |
| T-011     | Backend  | US-002 | 2h       | @gastonfr24 |
| T-012     | Backend  | US-002 | 2h       | @gastonfr24 |
| T-013     | Frontend | US-002 | 3h       | @gastonfr24 |
| T-014     | Frontend | US-002 | 3h       | @gastonfr24 |
| T-015     | Frontend | US-002 | 2h       | @gastonfr24 |
| T-016     | Backend  | US-003 | 1h       | @gastonfr24 |
| T-017     | Backend  | US-003 | 3h       | @gastonfr24 |
| T-018     | Frontend | US-003 | 4h       | @gastonfr24 |
| T-019     | Frontend | US-003 | 2h       | @gastonfr24 |
| T-020     | Backend  | US-004 | 3h       | @gastonfr24 |
| T-021     | Backend  | US-004 | 4h       | @gastonfr24 |
| T-022     | Frontend | US-004 | 2h       | @gastonfr24 |
| T-023     | Frontend | US-004 | 3h       | @gastonfr24 |
| T-024     | Frontend | US-004 | 2h       | @gastonfr24 |
| T-025     | Backend  | US-005 | 3h       | @gastonfr24 |
| T-026     | Frontend | US-005 | 3h       | @gastonfr24 |
| T-027     | Frontend | US-005 | 2h       | @gastonfr24 |
| **TOTAL** | -        | -      | **75h**  | -           |

**Estimado:** 75 horas de desarrollo  
**Disponibilidad:** 80 horas en 2 semanas (40h/semana)  
**Buffer:** 5 horas para imprevistos y testing

---

**Creado:** 27/01/2025  
**Última actualización:** 27/01/2025  
**Estado:** ✅ Listo para desarrollo
