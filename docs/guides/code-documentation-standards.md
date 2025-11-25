# 📝 Estándares de Documentación de Código

Este documento establece las reglas estrictas para documentar código en el proyecto Comercio.

## 🎯 Principios Fundamentales

### 1. Claridad sobre Brevedad
El código debe ser auto-explicativo, pero la documentación agrega contexto crucial.

### 2. Inglés para Código, Español para Comentarios
- **Nombres** (funciones, clases, variables): INGLÉS
- **Docstrings/JSDoc**: INGLÉS  
- **Comentarios explicativos**: ESPAÑOL

### 3. Sin Ruido
No documentar lo obvio. Solo agregar valor.

## 📋 Reglas Estrictas

### ✅ OBLIGATORIO

1. **Todas las funciones públicas** deben tener docstring/JSDoc
2. **Todos los parámetros** deben tener tipos definidos
3. **Clases y componentes complejos** deben estar documentados
4. **APIs públicas** requieren ejemplos de uso
5. **Excepciones** deben estar documentadas

### ❌ PROHIBIDO

1. **Emojis** en comentarios de código
2. **Historial de cambios** en comentarios (usar Git)
3. **Código comentado** (eliminar o usar Git)
4. **Comentarios obsoletos** o incorrectos
5. **TODO/FIXME** sin contexto o issue asociado
6. **Console.log/print** en código de producción

## 🐍 Python/Django - Estándares

### Docstrings - Google Style

```python
def calculate_order_total(
    order_id: int,
    apply_discount: bool = False,
    tax_rate: Optional[float] = None
) -> Decimal:
    """
    Calculate the total amount for an order including taxes and discounts.
    
    This function retrieves all order items, calculates subtotals,
    applies the specified tax rate (or retrieves it from settings),
    and optionally applies available discounts.
    
    Args:
        order_id: The unique identifier of the order
        apply_discount: Whether to apply available discount codes
        tax_rate: Custom tax rate to apply. If None, uses regional default
        
    Returns:
        The total order amount including taxes and discounts
        
    Raises:
        OrderNotFoundError: If the order does not exist
        InvalidOrderStateError: If the order is in an invalid state for calculation
        ValidationError: If tax_rate is negative or exceeds 1.0
        
    Example:
        >>> calculate_order_total(123, apply_discount=True)
        Decimal('159.99')
        
        >>> calculate_order_total(456, tax_rate=0.21)
        Decimal('242.50')
    """
```

### Clases

```python
class OrderService:
    """
    Service class for order management operations.
    
    This service handles all business logic related to orders,
    including creation, validation, payment processing, and
    status updates. It integrates with external payment providers
    and notification services.
    
    Attributes:
        payment_provider: Instance of the payment gateway adapter
        notification_service: Service for sending order notifications
        
    Example:
        >>> service = OrderService(payment_provider=StripeAdapter())
        >>> order = service.create_order(user_id=1, items=cart_items)
        >>> service.process_payment(order.id, payment_method='card')
    """
    
    def __init__(
        self,
        payment_provider: PaymentProvider,
        notification_service: Optional[NotificationService] = None
    ) -> None:
        """
        Initialize the OrderService with required dependencies.
        
        Args:
            payment_provider: Payment gateway adapter instance
            notification_service: Optional notification service for order updates
        """
        self.payment_provider = payment_provider
        self.notification_service = notification_service or EmailNotificationService()
```

### Módulos

```python
"""
Order management and processing services.

This module provides services for handling e-commerce orders,
including order creation, validation, payment processing,
fulfillment, and notifications.

Classes:
    OrderService: Main service for order operations
    OrderValidator: Validation logic for order data
    PaymentProcessor: Payment processing coordination

Functions:
    calculate_order_total: Calculate order totals with taxes
    validate_order_items: Validate order item availability

Example:
    >>> from apps.orders.services import OrderService
    >>> service = OrderService(payment_provider=StripeAdapter())
    >>> order = service.create_order(user_id=1, items=[...])
"""
```

## ⚛️ TypeScript/React - Estándares

### JSDoc para Componentes

```typescript
/**
 * ProductCard component displays product information with purchase actions.
 * 
 * This component renders a product card with image, title, price, and
 * action buttons. It supports multiple display modes (grid/list), handles
 * loading states, and manages add-to-cart interactions with optimistic updates.
 * 
 * @component
 * 
 * @example
 * ```tsx
 * <ProductCard 
 *   product={productData}
 *   onAddToCart={handleAddToCart}
 *   displayMode="grid"
 *   showQuickView
 * />
 * ```
 * 
 * @param props - Component props
 * @returns Rendered product card
 */
export function ProductCard({
  product,
  onAddToCart,
  displayMode = 'grid',
  showQuickView = false
}: ProductCardProps): JSX.Element {
  // Implementation
}
```

### Interfaces y Types

```typescript
/**
 * Props for the ProductCard component.
 */
interface ProductCardProps {
  /**
   * Product data to display.
   * Must include id, name, price, and at least one image.
   */
  product: Product
  
  /**
   * Callback fired when user clicks add to cart button.
   * Receives the product ID and selected quantity.
   */
  onAddToCart: (productId: string, quantity: number) => Promise<void>
  
  /**
   * Display mode for the card layout.
   * @default 'grid'
   */
  displayMode?: 'grid' | 'list'
  
  /**
   * Whether to show the quick view button.
   * @default false
   */
  showQuickView?: boolean
  
  /**
   * Optional CSS class name for custom styling.
   */
  className?: string
}

/**
 * Product data structure from the API.
 * 
 * Represents a product in the catalog with all necessary
 * information for display and purchase operations.
 */
interface Product {
  /** Unique product identifier (UUID v4) */
  id: string
  
  /** Product name (max 200 characters) */
  name: string
  
  /** URL-friendly product identifier */
  slug: string
  
  /** Product description in markdown format */
  description: string
  
  /** Price in USD (always positive) */
  price: number
  
  /** Product category */
  category: Category
  
  /** Array of product image URLs (ordered by display priority) */
  images: string[]
  
  /** Current stock availability */
  inStock: boolean
  
  /** Stock quantity (0 if out of stock) */
  stockQuantity: number
  
  /** Product creation timestamp (ISO 8601) */
  createdAt: string
}
```

### Hooks Personalizados

```typescript
/**
 * Custom hook for managing shopping cart state and operations.
 * 
 * This hook provides a complete cart management solution including:
 * - Add/remove items with quantity management
 * - Persistent storage in localStorage
 * - Automatic total calculations
 * - Optimistic UI updates
 * 
 * The cart state persists across page reloads and syncs with the backend
 * when the user is authenticated.
 * 
 * @returns Cart state and operation functions
 * 
 * @example
 * ```tsx
 * function CartPage() {
 *   const { items, total, addItem, removeItem, clearCart } = useCart()
 *   
 *   return (
 *     <div>
 *       <h1>Cart ({items.length} items)</h1>
 *       <p>Total: ${total.toFixed(2)}</p>
 *       <button onClick={clearCart}>Clear Cart</button>
 *     </div>
 *   )
 * }
 * ```
 */
export function useCart(): UseCartReturn {
  const [items, setItems] = useState<CartItem[]>([])
  const [isLoading, setIsLoading] = useState(false)
  
  /**
   * Add a product to the cart or increment quantity if already exists.
   * 
   * Performs optimistic update for better UX, then syncs with backend
   * if user is authenticated. Reverts on failure.
   * 
   * @param productId - The product ID to add
   * @param quantity - Quantity to add (must be positive)
   * @throws {Error} If product ID is invalid or quantity is not positive
   */
  const addItem = useCallback(async (
    productId: string,
    quantity: number = 1
  ): Promise<void> => {
    // Implementation
  }, [])
  
  return { items, total, isLoading, addItem, removeItem, clearCart }
}
```

### Funciones Utilitarias

```typescript
/**
 * Format a price value to localized currency string.
 * 
 * Formats numbers to USD currency with proper decimal places,
 * thousands separators, and optional symbol.
 * 
 * @param price - The price value to format (must be non-negative)
 * @param options - Formatting options
 * @returns Formatted price string
 * @throws {Error} If price is negative
 * 
 * @example
 * ```ts
 * formatPrice(29.99)
 * // "$29.99"
 * 
 * formatPrice(1234.5, { includeSymbol: false })
 * // "1,234.50"
 * 
 * formatPrice(9.5, { minimumFractionDigits: 0 })
 * // "$9.50"
 * ```
 */
export function formatPrice(
  price: number,
  options: FormatPriceOptions = {}
): string {
  const {
    includeSymbol = true,
    minimumFractionDigits = 2,
    maximumFractionDigits = 2,
  } = options
  
  if (price < 0) {
    throw new Error('Price cannot be negative')
  }
  
  const formatted = price.toLocaleString('en-US', {
    minimumFractionDigits,
    maximumFractionDigits,
  })
  
  return includeSymbol ? `$${formatted}` : formatted
}
```

## 💬 Comentarios en Código

### ✅ Buenos Comentarios

```python
# Validar permisos del usuario antes de proceder con la eliminación
if not user.has_permission('delete_order'):
    raise PermissionDeniedError()

# Aplicar descuento escalonado según el monto total
# 10% para compras mayores a $100
# 15% para compras mayores a $500
if total > 500:
    discount_rate = 0.15
elif total > 100:
    discount_rate = 0.10
else:
    discount_rate = 0.0

# Nota: La API de pagos requiere el monto en centavos
payment_amount = int(total * 100)
```

```typescript
// Filtrar productos agotados y ordenar por precio ascendente
const availableProducts = products
  .filter((p) => p.inStock)
  .sort((a, b) => a.price - b.price)

// Debounce search input para evitar requests excesivos
const debouncedSearch = useMemo(
  () => debounce(handleSearch, 300),
  [handleSearch]
)

// Prevenir scroll del body cuando el modal está abierto
useEffect(() => {
  if (isOpen) {
    document.body.style.overflow = 'hidden'
    return () => {
      document.body.style.overflow = 'unset'
    }
  }
}, [isOpen])
```

### ❌ Malos Comentarios

```python
# ❌ Comentario obvio - El código ya lo dice
counter += 1  # Incrementar contador

# ❌ Historial - Usar Git para esto
# Modificado por Juan el 2024-01-15
# Antes usaba filter(), ahora usa get()
user = User.objects.get(id=user_id)

# ❌ Código comentado - Eliminar o usar Git
# old_calculation = price * 0.9
# legacy_function(data)
new_calculation = calculate_discounted_price(price)

# ❌ Emojis en comentarios de producción
# 🚀 Super rápida función de cálculo

# ❌ Comentarios vagos sin contexto
# TODO: Arreglar esto
# Hack temporal
# Funciona pero hay que revisarlo

# ❌ Comentarios incorrectos u obsoletos
# Retorna True si el usuario es admin
return user.role == 'superuser'  # ¡El comentario está mal!
```

## 📝 Casos Especiales

### TODO/FIXME Aceptables

```python
# TODO(#123): Implementar paginación cuando el dataset crezca
# Current approach loads all items in memory, which is fine for
# the current dataset size (<1000 items) but will need pagination
# for scalability. GitHub issue #123 tracks this improvement.

# FIXME(#456): Race condition en concurrent cart updates
# Two simultaneous requests can cause inconsistent cart state.
# Needs transaction locking or optimistic concurrency control.
# See issue #456 for reproduction steps.
```

### Explicaciones de Algoritmos Complejos

```python
def calculate_shipping_cost(weight: float, distance: float) -> Decimal:
    """
    Calculate shipping cost using distance-weight pricing model.
    
    Algorithm:
    1. Base rate: $5.00 for first 100km
    2. Distance rate: $0.10 per additional km
    3. Weight surcharge: $0.50 per kg over 5kg
    4. Volume discount: 10% off for distances over 500km
    
    Args:
        weight: Package weight in kilograms
        distance: Shipping distance in kilometers
        
    Returns:
        Calculated shipping cost in USD
    """
    # Paso 1: Tarifa base
    base_rate = Decimal('5.00')
    
    # Paso 2: Cálculo de distancia
    if distance > 100:
        distance_cost = (distance - 100) * Decimal('0.10')
    else:
        distance_cost = Decimal('0')
    
    # Paso 3: Recargo por peso
    if weight > 5:
        weight_cost = (weight - 5) * Decimal('0.50')
    else:
        weight_cost = Decimal('0')
    
    # Paso 4: Cálculo total con descuento por volumen
    total = base_rate + distance_cost + weight_cost
    if distance > 500:
        total *= Decimal('0.90')  # 10% descuento
    
    return total.quantize(Decimal('0.01'))
```

## 🔍 Revisión de Código

### Checklist para Revisor

Al revisar PRs, verificar:

- [ ] Funciones públicas tienen documentación completa
- [ ] Parámetros y returns tienen tipos definidos
- [ ] Documentación coincide con implementación
- [ ] Ejemplos de uso son correctos y útiles
- [ ] No hay comentarios con emojis
- [ ] No hay código comentado sin razón
- [ ] No hay historial en comentarios
- [ ] Comentarios agregan valor (no son obvios)
- [ ] TODO/FIXME tienen issue asociado
- [ ] Sin console.log o print en producción

## 📚 Recursos

### Python
- [PEP 257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- [Sphinx Documentation](https://www.sphinx-doc.org/)

### TypeScript/JavaScript
- [TSDoc](https://tsdoc.org/)
- [JSDoc](https://jsdoc.app/)
- [TypeDoc](https://typedoc.org/)

### General
- [Clean Code by Robert C. Martin](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
- [Code Complete by Steve McConnell](https://www.microsoftpressstore.com/store/code-complete-9780735619678)

---

**Última actualización:** 2025-01-XX  
**Mantenedores:** @gastonfr24

