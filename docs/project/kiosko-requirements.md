# 🏪 Sistema de Kiosco - Requisitos del Cliente

## 📝 Pedido Original del Cliente

> "Quiero un sistema para un kiosco fácil, rápido, vistoso y muy ágil porque la persona que lo va a usar no sabe de PC. Necesito: stock, ventas, ganancias, pero sobre todo cobrar y caja."

---

## 🎯 Análisis de Requisitos

### Usuario Final

- **Perfil:** Persona sin conocimientos técnicos de PC
- **Necesidad:** Sistema intuitivo, visual, simple
- **Prioridad:** Velocidad en el cobro

### Funcionalidades Requeridas

#### 🔴 MUST HAVE (Crítico)

1. **Cobrar / Punto de Venta (POS)**

   - Interfaz grande y clara
   - Registro rápido de productos
   - Cálculo automático de totales
   - Múltiples formas de pago
   - Impresión de ticket

2. **Caja**

   - Apertura de caja
   - Cierre de caja
   - Arqueo de efectivo
   - Movimientos de caja

3. **Stock Básico**

   - Registro de productos
   - Control de stock actual
   - Alertas de stock bajo
   - Búsqueda rápida de productos

4. **Ventas**

   - Registro de ventas
   - Historial simple
   - Totales del día

5. **Ganancias Básicas**
   - Reporte de ventas del día
   - Ganancia total
   - Vista simple y clara

#### 🟡 SHOULD HAVE (Importante)

6. **Gestión de Productos**

   - Alta/Baja/Modificación de productos
   - Categorías
   - Precios y márgenes

7. **Reportes Básicos**

   - Ventas por período
   - Productos más vendidos
   - Movimientos de caja

8. **Gestión de Usuarios**
   - Login simple
   - Usuarios básicos (admin/cajero)

#### 🟢 COULD HAVE (Nice to have)

9. **Clientes Frecuentes**

   - Registro simple de clientes
   - Cuenta corriente básica

10. **Códigos de Barra**

    - Soporte para escáner
    - Búsqueda por código

11. **Backup Automático**
    - Respaldo de datos

---

## 🎨 Principios de Diseño

### UX/UI Requirements

1. **Simplicidad Extrema**

   - Botones grandes y claros
   - Colores contrastantes
   - Fuentes grandes y legibles
   - Mínimo texto, máximo íconos

2. **Velocidad**

   - Máximo 3 clicks para cualquier acción
   - Carga instantánea
   - Respuesta visual inmediata
   - Atajos de teclado

3. **Visual**

   - Interfaz moderna y atractiva
   - Feedback visual de acciones
   - Animaciones suaves
   - Estados claros

4. **Responsive**

   - Funciona en tablets
   - Funciona en pantallas táctiles
   - Adaptable a diferentes tamaños

5. **Tolerante a Errores**
   - Confirmaciones para acciones críticas
   - Deshacer operaciones
   - Mensajes de error claros
   - Recuperación de errores

---

## 🏗️ Arquitectura Propuesta

### Stack Tecnológico

**Backend:**

- Django 5.0 + REST Framework
- PostgreSQL
- Redis (cache)

**Frontend:**

- Next.js 14 (App Router)
- TypeScript
- Tailwind CSS + shadcn/ui
- Diseño optimizado para táctil

**Características:**

- PWA (Progressive Web App)
- Modo offline básico
- Impresión térmica (tickets)
- Soporte escáner código de barras

---

## 📊 Modelo de Datos Básico

```
┌─────────────┐
│   Product   │
├─────────────┤
│ id          │
│ barcode     │
│ name        │
│ price       │
│ cost        │
│ stock       │
│ category_id │
│ is_active   │
└─────────────┘
       │
       │ N
       │
       ▼ 1
┌─────────────┐      1  ┌─────────────┐
│    Sale     │◄────────│  CashRegister│
├─────────────┤         ├─────────────┤
│ id          │         │ id          │
│ total       │         │ opening_date│
│ payment_type│         │ closing_date│
│ date        │         │ opening_cash│
│ register_id │         │ closing_cash│
│ user_id     │         │ sales_total │
└─────────────┘         │ user_id     │
       │                └─────────────┘
       │ 1
       │
       ▼ N
┌─────────────┐
│  SaleItem   │
├─────────────┤
│ id          │
│ sale_id     │
│ product_id  │
│ quantity    │
│ unit_price  │
│ subtotal    │
└─────────────┘
```

---

## 🎯 Objetivos de Negocio

### Métricas de Éxito

1. **Velocidad de Cobro**

   - Tiempo promedio de venta: < 30 segundos
   - Desde escanear primer producto hasta imprimir ticket

2. **Facilidad de Uso**

   - Usuario nuevo puede realizar venta en < 5 minutos
   - Sin necesidad de capacitación extensa

3. **Confiabilidad**

   - 99.9% de uptime
   - Cero pérdida de datos
   - Backup automático diario

4. **Adopción**
   - Usuario final usa el sistema sin resistencia
   - Reporta que es más rápido que método anterior

---

## 🚀 Plan de Implementación

Ver: `docs/project/kiosko-sprint-plan.md` (próximo documento)

### Fases:

**Fase 1 - MVP (Sprint 1-2):** 4 semanas

- Sistema de ventas básico
- Caja simple
- Stock básico

**Fase 2 - Gestión (Sprint 3-4):** 4 semanas

- Gestión completa de productos
- Reportes básicos
- Usuarios

**Fase 3 - Avanzado (Sprint 5-6):** 4 semanas

- Clientes y cuenta corriente
- Reportes avanzados
- Optimizaciones

**Fase 4 - Pulido (Sprint 7):** 2 semanas

- Testing exhaustivo
- Ajustes de UX
- Capacitación

---

## 📋 Criterios de Aceptación Generales

### El sistema será aceptado cuando:

1. **Funcionalidad:**

   - ✅ Se pueden realizar ventas completas
   - ✅ Se abre y cierra caja correctamente
   - ✅ Stock se actualiza automáticamente
   - ✅ Reportes muestran datos correctos

2. **Usabilidad:**

   - ✅ Usuario sin conocimientos de PC puede operar
   - ✅ Venta completa en < 30 segundos
   - ✅ Interfaz intuitiva y clara

3. **Confiabilidad:**

   - ✅ No pierde ventas
   - ✅ Datos consistentes
   - ✅ Funciona offline básico

4. **Performance:**
   - ✅ Carga en < 2 segundos
   - ✅ Respuesta a clicks < 300ms
   - ✅ Búsqueda de productos < 1 segundo

---

**Fecha de Análisis:** 2025-01-XX  
**Analista:** @gastonfr24  
**Estado:** Aprobado para planificación de sprints
