# Sprint 1 - MVP: Punto de Venta Básico

**Fecha Inicio:** 27/01/2025  
**Fecha Fin:** 09/02/2025  
**Duración:** 2 semanas  
**Velocity Objetivo:** 30 story points

---

## 🎯 Objetivo del Sprint

Crear un sistema funcional completo que permita:

- Registrar productos en el sistema
- Realizar ventas de forma rápida y visual
- Cobrar en efectivo y tarjeta
- Abrir y cerrar caja diariamente
- Ver ventas del día
- **Autenticación segura con JWT**
- **Dashboard administrativo profesional**
- **Interfaz ultra simple para usuarios no técnicos**

**Resultado esperado:** Un kiosco puede operar completamente con autenticación, roles de usuario y dashboard profesional.

---

## 📋 User Stories Seleccionadas

### US-001: Registro rápido de venta

- **Story Points:** 8
- **Prioridad:** 🔴 Alta
- **Asignado a:** @gastonfr24

### US-002: Gestión básica de productos

- **Story Points:** 5
- **Prioridad:** 🔴 Alta
- **Asignado a:** @gastonfr24

### US-003: Cobro y métodos de pago

- **Story Points:** 8
- **Prioridad:** 🔴 Alta
- **Asignado a:** @gastonfr24

### US-004: Apertura/Cierre de caja básico

- **Story Points:** 5
- **Prioridad:** 🔴 Alta
- **Asignado a:** @gastonfr24

### US-005: Vista de ventas del día

- **Story Points:** 4
- **Prioridad:** 🔴 Alta
- **Asignado a:** @gastonfr24

### US-006: Sistema de autenticación JWT

- **Story Points:** 13
- **Prioridad:** 🔴 Alta
- **Asignado a:** @gastonfr24
- **Descripción:** Sistema completo de autenticación con roles (admin, cajero)

### US-007: Dashboard administrativo profesional

- **Story Points:** 13
- **Prioridad:** 🟡 Media
- **Asignado a:** @gastonfr24
- **Descripción:** Dashboard con métricas, gráficos y accesos rápidos

### US-008: Mejorar interfaz simple del POS

- **Story Points:** 8
- **Prioridad:** 🟡 Media
- **Asignado a:** @gastonfr24
- **Descripción:** UX optimizada para usuarios sin experiencia en PC

---

## 📊 Métricas

- **Total Story Points:** 64 (30 originales + 34 nuevos)
- **Tareas Totales:** 45 (ver user-stories.md)
- **Velocity Anterior:** N/A (primer sprint)
- **Velocity Objetivo (Ajustado):** 64
- **Horas Estimadas:** 139 horas

---

## 👥 Team

- **Product Owner:** Cliente de Kiosco
- **Scrum Master:** @gastonfr24
- **Developer:** @gastonfr24

---

## 🎯 Definition of Done (Sprint 1)

### Código:

- [ ] Todas las tareas completadas
- [ ] Tests unitarios escritos y pasando
- [ ] Sin errores de linter
- [ ] Código documentado (docstrings/JSDoc)

### Funcionalidad:

- [ ] Se pueden crear productos
- [ ] Se pueden registrar ventas completas
- [ ] Se puede cobrar y elegir método de pago
- [ ] Se puede abrir y cerrar caja
- [ ] Se muestra reporte de ventas del día

### Documentación:

- [ ] CHANGELOG.md actualizado
- [ ] docs/api/ con endpoints creados
- [ ] docs/architecture/ actualizado
- [ ] README actualizado con setup

### Calidad:

- [ ] Sistema opera en < 2 segundos
- [ ] Venta completa en < 30 segundos
- [ ] UI clara y grande (usuario sin experiencia PC)

---

## 🏗️ Arquitectura Técnica

### Backend (Sprint 1)

```
apps/
├── products/
│   ├── models.py       # Product model
│   ├── serializers.py  # ProductSerializer
│   ├── views.py        # ProductViewSet
│   └── urls.py         # /api/products/
│
├── sales/
│   ├── models.py       # Sale, SaleItem models
│   ├── serializers.py  # SaleSerializer
│   ├── views.py        # SaleViewSet
│   └── urls.py         # /api/sales/
│
├── cash_register/
│   ├── models.py       # CashRegister model
│   ├── serializers.py  # CashRegisterSerializer
│   ├── views.py        # CashRegisterViewSet
│   └── urls.py         # /api/cash-register/
│
└── users/              # NUEVO: Autenticación
    ├── models.py       # Custom User model con roles
    ├── serializers.py  # UserSerializer, RegisterSerializer
    ├── views.py        # Auth endpoints
    └── urls.py         # /api/auth/
```

### Frontend (Sprint 1)

```
src/
├── app/
│   ├── (public)/      # NUEVO: Rutas públicas
│   │   └── login/     # Página de login
│   │
│   ├── (protected)/   # NUEVO: Rutas protegidas
│   │   ├── dashboard/ # Dashboard administrativo (admin only)
│   │   ├── pos/       # Página principal de ventas
│   │   ├── products/  # Gestión de productos
│   │   ├── cash/      # Apertura/cierre de caja
│   │   └── reports/   # Reporte de ventas
│   │
│   └── layout.tsx     # Layout global con AuthProvider
│
├── components/
│   ├── auth/          # NUEVO: Autenticación
│   │   ├── LoginForm.tsx
│   │   ├── ProtectedRoute.tsx
│   │   └── AuthProvider.tsx
│   │
│   ├── layout/        # NUEVO: Layouts
│   │   ├── AdminLayout.tsx      # Sidebar + Header
│   │   ├── Sidebar.tsx
│   │   └── Header.tsx
│   │
│   ├── dashboard/     # NUEVO: Dashboard
│   │   ├── StatsCards.tsx
│   │   ├── SalesChart.tsx
│   │   ├── QuickActions.tsx
│   │   └── TopProducts.tsx
│   │
│   ├── pos/
│   │   ├── ScannerInput.tsx
│   │   ├── ProductList.tsx
│   │   ├── CartSummary.tsx
│   │   ├── PaymentModal.tsx
│   │   └── NumericKeyboard.tsx  # NUEVO: Teclado en pantalla
│   │
│   ├── products/
│   │   ├── ProductForm.tsx
│   │   └── ProductTable.tsx
│   │
│   └── cash/
│       ├── OpenCashForm.tsx
│       └── CloseCashForm.tsx
│
├── contexts/          # NUEVO: Contexts
│   └── AuthContext.tsx
│
└── lib/
    ├── api/
    │   ├── auth.ts         # NUEVO: Auth API
    │   ├── dashboard.ts    # NUEVO: Dashboard API
    │   ├── products.ts
    │   ├── sales.ts
    │   └── cash-register.ts
    └── hooks/
        ├── useAuth.ts      # NUEVO: Auth hook
        ├── useCart.ts
        └── useCashRegister.ts
```

---

## 🔧 Stack Técnico Confirmado

### Backend:

- Django 5.0
- Django REST Framework
- SQLite (desarrollo)
- pytest para testing

### Frontend:

- Next.js 14 (App Router)
- TypeScript
- Tailwind CSS + shadcn/ui
- Diseño optimizado para táctil

---

## 📅 Planning Detallado

### Semana 1 (27/01 - 02/02)

**Lunes 27/01 - Sprint Planning**

- ✅ Planning meeting (2 horas)
- ✅ Setup de documentación
- 🎯 Iniciar T-001: Product model

**Martes 28/01 - Jueves 30/01**

- Backend: Modelos y APIs de productos
- T-001 a T-005

**Viernes 31/01 - Domingo 02/02**

- Backend: Modelos y APIs de ventas
- T-006 a T-010

### Semana 2 (03/02 - 09/02)

**Lunes 03/02 - Miércoles 05/02**

- Frontend: Componentes de POS
- T-011 a T-015

**Jueves 06/02 - Viernes 07/02**

- Frontend: Gestión de productos y caja
- T-016 a T-020
- Testing e integración

**Sábado 08/02 - Domingo 09/02**

- Testing completo
- Ajustes de UX
- Documentación final
- Sprint Review
- Sprint Retrospective

---

## 🚧 Impedimentos Potenciales

1. **Escáner de código de barras**

   - Plan A: Integrar escáner real
   - Plan B: Input manual de código
   - Decisión: Semana 1

2. **Impresora térmica para tickets**

   - Plan A: Integración con impresora
   - Plan B: Vista para imprimir en navegador
   - Decisión: Sprint 2 (no crítico)

3. **Performance con muchos productos**
   - Solución: Paginación desde inicio
   - Búsqueda con debounce

---

## 📝 Notas del Planning

### Decisiones Tomadas:

1. **Autenticación:** (NUEVO)

   - JWT con djangorestframework-simplejwt
   - Roles: ADMIN (gestión completa), CASHIER (solo ventas)
   - Refresh tokens con rotación
   - Logout con blacklist de tokens

2. **Dashboard:** (NUEVO)

   - Solo accesible para usuarios ADMIN
   - Gráficos con recharts library
   - Métricas en tiempo real
   - Diseño profesional con sidebar colapsable

3. **UI/UX:**

   - **POS Simple:** Botones grandes (mínimo 48x48px), fuente grande (18px+)
   - **Dashboard Admin:** Interfaz profesional estilo SaaS moderno
   - Dos modos: Simple (cajero) y Avanzado (admin)
   - Colores contrastantes
   - Máximo 3 clicks para cualquier acción

4. **Métodos de pago:**

   - Efectivo
   - Tarjeta (débito/crédito)
   - Otros (transferencia)
   - **MercadoPago** (integración planificada)

5. **Flujo de venta:**

   - Escanear/Buscar producto
   - Agregar al carrito (lista visible)
   - Ver total en tiempo real
   - Botón grande "COBRAR"
   - Seleccionar método de pago
   - Confirmar (opcional: imprimir ticket)

6. **Caja:**
   - Abrir caja al inicio del día (monto inicial)
   - Registrar ventas normalmente
   - Cerrar caja (contar efectivo, ver diferencias)

---

## 🎯 Criterios de Éxito del Sprint

El Sprint 1 será exitoso si:

1. **Funcionalidad Core:**

   - ✅ Puedo registrarme e iniciar sesión con JWT
   - ✅ Hay roles diferenciados (admin, cajero)
   - ✅ Puedo crear 10 productos en < 5 minutos
   - ✅ Puedo hacer una venta completa en < 30 segundos
   - ✅ El stock se descuenta automáticamente
   - ✅ Puedo ver total de ventas del día
   - ✅ Dashboard muestra métricas clave con gráficos

2. **Calidad:**

   - ✅ Zero bugs críticos
   - ✅ Tests pasando (>70% coverage)
   - ✅ UI simple del POS es usable por persona sin experiencia PC
   - ✅ Dashboard profesional cumple estándares modernos

3. **Seguridad:**

   - ✅ Autenticación JWT funcionando
   - ✅ Rutas protegidas verifican roles
   - ✅ Tokens expiran correctamente
   - ✅ No hay vulnerabilidades de seguridad básicas

4. **Técnico:**
   - ✅ Código sigue .cursorrules
   - ✅ Documentación actualizada
   - ✅ Deploy funciona en localhost
   - ✅ Hot reload funciona en Docker

---

## 📞 Comunicación

### Daily Standups:

- **Hora:** 9:00 AM (o async si solo)
- **Formato:** Ver sprint-workflow.md
- **Registro:** Actualizar progress.md diariamente

### Sprint Review:

- **Fecha:** 09/02/2025
- **Duración:** 1 hora
- **Demo:** Hacer venta completa en vivo

### Sprint Retrospective:

- **Fecha:** 09/02/2025
- **Duración:** 30 minutos
- **Documentar en:** retrospective.md

---

**Fecha de Planning:** 27/01/2025  
**Próxima revisión:** 03/02/2025 (mid-sprint check)  
**Estado:** 🟢 Aprobado para iniciar
