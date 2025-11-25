# 📖 Ejemplos Prácticos de Documentación

Esta guía contiene ejemplos reales de cómo documentar código correctamente en el proyecto.

## 🐍 Ejemplos Python/Django

### ✅ Modelo Bien Documentado

```python
"""
Models for the products application.
"""
from django.db import models
from django.contrib.auth.models import User
from typing import Optional
from decimal import Decimal


class Product(models.Model):
    """
    Product model representing items in the catalog.
    
    Each product belongs to a category and can have multiple variants.
    Prices are stored in USD with 2 decimal precision. Products can be
    marked as featured for homepage display.
    
    Attributes:
        name: Product name (max 200 characters)
        slug: URL-friendly identifier
        description: Full product description (markdown supported)
        price: Product price in USD
        category: Foreign key to Category model
        is_active: Whether the product is visible in the catalog
        is_featured: Whether to display on homepage
        stock_quantity: Current inventory count
        created_at: Product creation timestamp
        updated_at: Last modification timestamp
    """
    
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='products'
    )
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    stock_quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['category', 'is_active']),
        ]
    
    def __str__(self) -> str:
        return self.name
    
    def is_in_stock(self) -> bool:
        """
        Check if product has available inventory.
        
        Returns:
            True if stock_quantity > 0, False otherwise
        """
        return self.stock_quantity > 0
    
    def apply_discount(self, percentage: float) -> Decimal:
        """
        Calculate discounted price for the product.
        
        Args:
            percentage: Discount percentage (0-100)
            
        Returns:
            Discounted price rounded to 2 decimal places
            
        Raises:
            ValueError: If percentage is not between 0 and 100
            
        Example:
            >>> product.price = Decimal('100.00')
            >>> product.apply_discount(20)
            Decimal('80.00')
        """
        if not 0 <= percentage <= 100:
            raise ValueError("Percentage must be between 0 and 100")
        
        discount_multiplier = Decimal(1) - (Decimal(percentage) / Decimal(100))
        discounted_price = self.price * discount_multiplier
        
        return discounted_price.quantize(Decimal('0.01'))
    
    def reduce_stock(self, quantity: int) -> None:
        """
        Reduce stock quantity after purchase.
        
        Updates the stock_quantity and saves the model. Does not allow
        stock to go negative - raises exception instead.
        
        Args:
            quantity: Number of units to reduce
            
        Raises:
            ValueError: If quantity exceeds available stock
            
        Example:
            >>> product.stock_quantity = 10
            >>> product.reduce_stock(3)
            >>> product.stock_quantity
            7
        """
        if quantity > self.stock_quantity:
            raise ValueError(
                f"Cannot reduce stock by {quantity}. "
                f"Only {self.stock_quantity} units available."
            )
        
        self.stock_quantity -= quantity
        self.save(update_fields=['stock_quantity', 'updated_at'])
```

### ✅ View Bien Documentada

```python
"""
API views for product management.
"""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.db.models import Q
from typing import Any
import logging

logger = logging.getLogger(__name__)


class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet for product CRUD operations and custom actions.
    
    Provides standard endpoints for listing, creating, retrieving,
    updating, and deleting products. Includes custom actions for
    searching, filtering by category, and managing featured products.
    
    Permissions:
        - List/Retrieve: Public (no authentication required)
        - Create/Update/Delete: Admin only
        - Feature/Unfeature: Admin only
        
    Endpoints:
        GET    /api/products/          - List all products
        POST   /api/products/          - Create product (admin)
        GET    /api/products/{id}/     - Retrieve product
        PUT    /api/products/{id}/     - Update product (admin)
        DELETE /api/products/{id}/     - Delete product (admin)
        GET    /api/products/search/   - Search products
        POST   /api/products/{id}/feature/ - Mark as featured (admin)
    """
    
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    
    def get_permissions(self):
        """
        Set permissions based on action.
        
        Returns:
            List of permission instances
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy', 'feature']:
            return [IsAdminUser()]
        return []
    
    @action(detail=False, methods=['get'])
    def search(self, request: Any) -> Response:
        """
        Search products by name or description.
        
        Performs case-insensitive search across product name and description
        fields. Returns paginated results matching the search query.
        
        Query Parameters:
            q (str): Search query string (required)
            
        Returns:
            Response with list of matching products
            
        Example:
            GET /api/products/search/?q=laptop
            
            Response:
            {
                "count": 5,
                "results": [
                    {
                        "id": 1,
                        "name": "Gaming Laptop",
                        "price": "999.99",
                        ...
                    }
                ]
            }
        """
        query = request.query_params.get('q', '').strip()
        
        if not query:
            return Response(
                {"error": "Search query parameter 'q' is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Buscar en nombre y descripción
        products = self.get_queryset().filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )
        
        # Paginar resultados
        page = self.paginate_queryset(products)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def feature(self, request: Any, pk: Optional[int] = None) -> Response:
        """
        Mark product as featured for homepage display.
        
        Featured products appear on the homepage and in promotional banners.
        Only admin users can feature/unfeature products.
        
        Args:
            pk: Product ID
            
        Returns:
            Response with updated product data
            
        Raises:
            404: If product not found
            403: If user is not admin
            
        Example:
            POST /api/products/123/feature/
            
            Response:
            {
                "id": 123,
                "name": "Product Name",
                "is_featured": true,
                ...
            }
        """
        product = self.get_object()
        product.is_featured = True
        product.save(update_fields=['is_featured', 'updated_at'])
        
        logger.info(
            f"Product {product.id} marked as featured by user {request.user.id}"
        )
        
        serializer = self.get_serializer(product)
        return Response(serializer.data)
```

## ⚛️ Ejemplos TypeScript/React

### ✅ Componente Bien Documentado

```typescript
'use client'

import { useState, useCallback } from 'react'
import { Card, CardHeader, CardTitle, CardContent, CardFooter } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import { ShoppingCart, Heart } from 'lucide-react'
import { formatPrice } from '@/lib/utils'
import type { Product } from '@/types'

/**
 * Props for the ProductCard component.
 */
interface ProductCardProps {
  /**
   * Product data to display.
   * Must include id, name, price, and images array.
   */
  product: Product
  
  /**
   * Callback fired when user clicks add to cart.
   * Should handle adding the product to cart state.
   */
  onAddToCart: (productId: string) => Promise<void>
  
  /**
   * Optional callback for adding to wishlist.
   * If not provided, wishlist button will not be shown.
   */
  onAddToWishlist?: (productId: string) => Promise<void>
  
  /**
   * Display mode for the card.
   * @default 'grid'
   */
  displayMode?: 'grid' | 'list'
  
  /**
   * Optional CSS class name for styling.
   */
  className?: string
}

/**
 * ProductCard displays a single product with purchase actions.
 * 
 * This component renders a product card with image, title, price,
 * stock status, and action buttons. It handles loading states during
 * async operations and provides visual feedback to the user.
 * 
 * Features:
 * - Responsive image display
 * - Stock status indicator
 * - Add to cart with loading state
 * - Optional wishlist functionality
 * - Grid and list display modes
 * 
 * @component
 * 
 * @example
 * ```tsx
 * <ProductCard 
 *   product={productData}
 *   onAddToCart={handleAddToCart}
 *   onAddToWishlist={handleAddToWishlist}
 *   displayMode="grid"
 * />
 * ```
 */
export function ProductCard({
  product,
  onAddToCart,
  onAddToWishlist,
  displayMode = 'grid',
  className
}: ProductCardProps) {
  const [isAddingToCart, setIsAddingToCart] = useState(false)
  const [isAddingToWishlist, setIsAddingToWishlist] = useState(false)
  
  /**
   * Handle add to cart button click.
   * 
   * Shows loading state during the operation and handles errors
   * with user-friendly messages. Disables button during operation
   * to prevent duplicate requests.
   */
  const handleAddToCart = useCallback(async () => {
    if (!product.inStock || isAddingToCart) return
    
    setIsAddingToCart(true)
    try {
      await onAddToCart(product.id)
    } catch (error) {
      console.error('Failed to add product to cart:', error)
      // Error handling logic (toast notification, etc.)
    } finally {
      setIsAddingToCart(false)
    }
  }, [product.id, product.inStock, isAddingToCart, onAddToCart])
  
  /**
   * Handle wishlist button click.
   * 
   * Similar to cart handling but for wishlist. Only executed
   * if onAddToWishlist callback is provided.
   */
  const handleAddToWishlist = useCallback(async () => {
    if (!onAddToWishlist || isAddingToWishlist) return
    
    setIsAddingToWishlist(true)
    try {
      await onAddToWishlist(product.id)
    } catch (error) {
      console.error('Failed to add product to wishlist:', error)
    } finally {
      setIsAddingToWishlist(false)
    }
  }, [product.id, isAddingToWishlist, onAddToWishlist])
  
  return (
    <Card className={className}>
      <CardHeader>
        <div className="relative">
          <img
            src={product.images[0]}
            alt={product.name}
            className="w-full h-48 object-cover rounded-t-lg"
          />
          {!product.inStock && (
            <Badge
              variant="destructive"
              className="absolute top-2 right-2"
            >
              Out of Stock
            </Badge>
          )}
        </div>
        <CardTitle className="mt-4">{product.name}</CardTitle>
      </CardHeader>
      
      <CardContent>
        <p className="text-2xl font-bold text-primary">
          {formatPrice(product.price)}
        </p>
        <p className="text-sm text-muted-foreground mt-2 line-clamp-2">
          {product.description}
        </p>
      </CardContent>
      
      <CardFooter className="flex gap-2">
        <Button
          onClick={handleAddToCart}
          disabled={!product.inStock || isAddingToCart}
          className="flex-1"
        >
          <ShoppingCart className="mr-2 h-4 w-4" />
          {isAddingToCart ? 'Adding...' : 'Add to Cart'}
        </Button>
        
        {onAddToWishlist && (
          <Button
            variant="outline"
            onClick={handleAddToWishlist}
            disabled={isAddingToWishlist}
          >
            <Heart className="h-4 w-4" />
          </Button>
        )}
      </CardFooter>
    </Card>
  )
}
```

### ✅ Hook Personalizado Bien Documentado

```typescript
'use client'

import { useState, useEffect, useCallback } from 'react'
import { useRouter } from 'next/navigation'
import type { CartItem, Product } from '@/types'

/**
 * Return type for the useCart hook.
 */
interface UseCartReturn {
  /** Array of items currently in the cart */
  items: CartItem[]
  
  /** Total price of all items in cart */
  total: number
  
  /** Number of items in cart */
  itemCount: number
  
  /** Whether cart operations are in progress */
  isLoading: boolean
  
  /** Add item to cart */
  addItem: (productId: string, quantity?: number) => Promise<void>
  
  /** Remove item from cart */
  removeItem: (productId: string) => Promise<void>
  
  /** Update item quantity */
  updateQuantity: (productId: string, quantity: number) => Promise<void>
  
  /** Clear all items from cart */
  clearCart: () => Promise<void>
}

/**
 * Custom hook for managing shopping cart state.
 * 
 * This hook provides a complete cart management solution with:
 * - Persistent storage in localStorage
 * - Automatic total calculations
 * - Backend synchronization for authenticated users
 * - Optimistic UI updates for better UX
 * 
 * The cart persists across page reloads and syncs with the backend
 * API when the user is authenticated. For guest users, cart data
 * is stored only in localStorage.
 * 
 * @returns Cart state and operation functions
 * 
 * @example
 * ```tsx
 * function CartPage() {
 *   const { 
 *     items, 
 *     total, 
 *     itemCount,
 *     addItem, 
 *     removeItem,
 *     clearCart
 *   } = useCart()
 *   
 *   return (
 *     <div>
 *       <h1>Cart ({itemCount} items)</h1>
 *       <p>Total: ${total.toFixed(2)}</p>
 *       {items.map(item => (
 *         <div key={item.productId}>
 *           {item.product.name} x {item.quantity}
 *           <button onClick={() => removeItem(item.productId)}>
 *             Remove
 *           </button>
 *         </div>
 *       ))}
 *       <button onClick={clearCart}>Clear Cart</button>
 *     </div>
 *   )
 * }
 * ```
 */
export function useCart(): UseCartReturn {
  const router = useRouter()
  const [items, setItems] = useState<CartItem[]>([])
  const [isLoading, setIsLoading] = useState(false)
  
  /**
   * Load cart from localStorage on mount.
   * Runs once when the component mounts.
   */
  useEffect(() => {
    const stored = localStorage.getItem('cart')
    if (stored) {
      try {
        const parsed = JSON.parse(stored)
        setItems(parsed)
      } catch (error) {
        console.error('Failed to parse cart from localStorage:', error)
        localStorage.removeItem('cart')
      }
    }
  }, [])
  
  /**
   * Save cart to localStorage whenever items change.
   */
  useEffect(() => {
    localStorage.setItem('cart', JSON.stringify(items))
  }, [items])
  
  /**
   * Calculate total price of all items in cart.
   */
  const total = items.reduce(
    (sum, item) => sum + (item.product.price * item.quantity),
    0
  )
  
  /**
   * Calculate total number of items in cart.
   */
  const itemCount = items.reduce((sum, item) => sum + item.quantity, 0)
  
  /**
   * Add a product to the cart or increment quantity if it exists.
   * 
   * Performs optimistic update for better UX, then attempts to sync
   * with backend. If sync fails, reverts the optimistic update.
   * 
   * @param productId - The product ID to add
   * @param quantity - Quantity to add (default: 1)
   * @throws {Error} If productId is invalid or quantity is not positive
   * 
   * @example
   * ```ts
   * await addItem('product-123', 2)
   * ```
   */
  const addItem = useCallback(async (
    productId: string,
    quantity: number = 1
  ): Promise<void> => {
    if (!productId || quantity < 1) {
      throw new Error('Invalid product ID or quantity')
    }
    
    setIsLoading(true)
    
    // Optimistic update
    setItems(prevItems => {
      const existingItem = prevItems.find(item => item.productId === productId)
      
      if (existingItem) {
        return prevItems.map(item =>
          item.productId === productId
            ? { ...item, quantity: item.quantity + quantity }
            : item
        )
      } else {
        // Fetch product data would happen here
        // For now, assuming we have the product
        return [...prevItems, { productId, quantity, product: {} as Product }]
      }
    })
    
    try {
      // Sync with backend API
      // await api.post('/cart/items', { productId, quantity })
    } catch (error) {
      // Revert optimistic update on error
      console.error('Failed to add item to cart:', error)
      throw error
    } finally {
      setIsLoading(false)
    }
  }, [])
  
  /**
   * Remove a product from the cart completely.
   * 
   * @param productId - The product ID to remove
   * 
   * @example
   * ```ts
   * await removeItem('product-123')
   * ```
   */
  const removeItem = useCallback(async (productId: string): Promise<void> => {
    setIsLoading(true)
    
    setItems(prevItems => prevItems.filter(item => item.productId !== productId))
    
    try {
      // await api.delete(`/cart/items/${productId}`)
    } catch (error) {
      console.error('Failed to remove item from cart:', error)
    } finally {
      setIsLoading(false)
    }
  }, [])
  
  /**
   * Update the quantity of a product in the cart.
   * 
   * @param productId - The product ID to update
   * @param quantity - New quantity (must be positive, use removeItem for zero)
   * 
   * @example
   * ```ts
   * await updateQuantity('product-123', 5)
   * ```
   */
  const updateQuantity = useCallback(async (
    productId: string,
    quantity: number
  ): Promise<void> => {
    if (quantity < 1) {
      throw new Error('Quantity must be at least 1. Use removeItem for zero.')
    }
    
    setIsLoading(true)
    
    setItems(prevItems =>
      prevItems.map(item =>
        item.productId === productId
          ? { ...item, quantity }
          : item
      )
    )
    
    try {
      // await api.patch(`/cart/items/${productId}`, { quantity })
    } catch (error) {
      console.error('Failed to update item quantity:', error)
    } finally {
      setIsLoading(false)
    }
  }, [])
  
  /**
   * Clear all items from the cart.
   * Shows confirmation dialog before clearing.
   * 
   * @example
   * ```ts
   * await clearCart()
   * ```
   */
  const clearCart = useCallback(async (): Promise<void> => {
    if (!confirm('Are you sure you want to clear your cart?')) {
      return
    }
    
    setIsLoading(true)
    setItems([])
    
    try {
      // await api.delete('/cart')
    } catch (error) {
      console.error('Failed to clear cart:', error)
    } finally {
      setIsLoading(false)
    }
  }, [])
  
  return {
    items,
    total,
    itemCount,
    isLoading,
    addItem,
    removeItem,
    updateQuantity,
    clearCart,
  }
}
```

## 💬 Comentarios Apropiados

### ✅ Buenos Comentarios

```python
# Aplicar descuento escalonado según monto de compra
if total > 500:
    discount = 0.15  # 15% para compras mayores a $500
elif total > 100:
    discount = 0.10  # 10% para compras mayores a $100
else:
    discount = 0.0

# La API de pagos requiere el monto en centavos
payment_amount = int(total * 100)

# Cache invalidation: limpiar cache de productos cuando cambie el inventario
cache.delete_pattern('products:*')
```

```typescript
// Debounce de búsqueda para reducir requests al API
const debouncedSearch = useDebouncedCallback(
  (value: string) => {
    performSearch(value)
  },
  300 // Esperar 300ms después del último keystroke
)

// Prevenir scroll del body cuando el modal está abierto
useEffect(() => {
  if (isModalOpen) {
    document.body.style.overflow = 'hidden'
    return () => {
      document.body.style.overflow = 'unset'
    }
  }
}, [isModalOpen])
```

### ❌ Malos Comentarios

```python
# ❌ Comentario obvio
counter += 1  # Incrementar contador

# ❌ Historial de cambios
# Modificado por Juan el 2024-01-15
# Antes usaba get(), ahora usa filter()
products = Product.objects.filter(active=True)

# ❌ Código comentado
# old_function()
# previous_implementation = legacy_code()

# ❌ Emojis
# 🚀 Función super rápida

# ❌ Comentarios vagos
# TODO: arreglar esto
# Hack temporal
```

---

**Última actualización:** 2025-01-XX  
**Mantenedores:** @gastonfr24

