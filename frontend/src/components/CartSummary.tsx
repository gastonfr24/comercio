"use client";

import React from "react";
import { Minus, Plus, Trash2, ShoppingCart } from "lucide-react";
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { CartItem } from "@/hooks/useCart";

interface CartSummaryProps {
  items: CartItem[];
  totals: {
    subtotal: number;
    itemCount: number;
  };
  // eslint-disable-next-line no-unused-vars
  onIncrement: (productId: number) => void;
  // eslint-disable-next-line no-unused-vars
  onDecrement: (productId: number) => void;
  // eslint-disable-next-line no-unused-vars
  onRemove: (productId: number) => void;
  onClear: () => void;
  onCheckout?: () => void;
  isCheckoutDisabled?: boolean;
}

/**
 * CartSummary component for displaying cart items and totals.
 *
 * Shows full cart contents with quantity controls and total calculation.
 * Optimized for POS quick checkout.
 *
 * @param items - Array of cart items
 * @param totals - Cart totals (subtotal, itemCount)
 * @param onIncrement - Callback to increment item quantity
 * @param onDecrement - Callback to decrement item quantity
 * @param onRemove - Callback to remove item
 * @param onClear - Callback to clear entire cart
 * @param onCheckout - Callback for checkout action
 * @param isCheckoutDisabled - Disable checkout button
 */
export function CartSummary({
  items,
  totals,
  onIncrement,
  onDecrement,
  onRemove,
  onClear,
  onCheckout,
  isCheckoutDisabled = false,
}: CartSummaryProps) {
  /**
   * Format price to currency.
   */
  const formatPrice = (price: number): string => {
    return new Intl.NumberFormat("es-AR", {
      style: "currency",
      currency: "ARS",
    }).format(price);
  };

  /**
   * Calculate item subtotal.
   */
  const getItemSubtotal = (item: CartItem): number => {
    return item.price * item.quantity;
  };

  // Empty cart state
  if (items.length === 0) {
    return (
      <Card>
        <CardHeader>
          <CardTitle>Carrito</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="flex flex-col items-center justify-center py-8 text-center">
            <ShoppingCart className="h-16 w-16 text-muted-foreground mb-4" />
            <h3 className="text-lg font-semibold mb-2">Carrito vacío</h3>
            <p className="text-muted-foreground text-sm max-w-sm">
              Busca y agrega productos para comenzar una venta
            </p>
          </div>
        </CardContent>
      </Card>
    );
  }

  // Cart with items
  return (
    <Card>
      <CardHeader>
        <div className="flex items-center justify-between">
          <CardTitle>
            Carrito
            <Badge variant="secondary" className="ml-2">
              {totals.itemCount} {totals.itemCount === 1 ? "item" : "items"}
            </Badge>
          </CardTitle>
          <Button variant="ghost" size="sm" onClick={onClear}>
            Limpiar
          </Button>
        </div>
      </CardHeader>

      <CardContent className="space-y-3">
        {items.map((item) => (
          <div
            key={item.id}
            className="flex items-center gap-3 p-3 bg-muted/50 rounded-lg"
          >
            {/* Product Info */}
            <div className="flex-1 min-w-0">
              <h4 className="font-semibold text-sm line-clamp-1">{item.name}</h4>
              <p className="text-xs text-muted-foreground">{item.barcode}</p>
              <p className="text-sm font-medium mt-1">
                {formatPrice(item.price)} x {item.quantity}
              </p>
            </div>

            {/* Quantity Controls */}
            <div className="flex items-center gap-1">
              <Button
                variant="outline"
                size="icon"
                className="h-8 w-8"
                onClick={() => onDecrement(item.id)}
                aria-label="Disminuir cantidad"
              >
                <Minus className="h-4 w-4" />
              </Button>

              <div className="w-12 text-center">
                <span className="text-lg font-bold">{item.quantity}</span>
              </div>

              <Button
                variant="outline"
                size="icon"
                className="h-8 w-8"
                onClick={() => onIncrement(item.id)}
                aria-label="Aumentar cantidad"
              >
                <Plus className="h-4 w-4" />
              </Button>
            </div>

            {/* Subtotal and Remove */}
            <div className="flex flex-col items-end gap-2">
              <p className="text-lg font-bold">
                {formatPrice(getItemSubtotal(item))}
              </p>
              <Button
                variant="ghost"
                size="sm"
                className="h-7 w-7 p-0 text-destructive hover:text-destructive"
                onClick={() => onRemove(item.id)}
                aria-label="Eliminar producto"
              >
                <Trash2 className="h-4 w-4" />
              </Button>
            </div>
          </div>
        ))}
      </CardContent>

      <CardFooter className="flex-col gap-4">
        {/* Total Section */}
        <div className="w-full space-y-2 p-4 bg-muted/30 rounded-lg">
          <div className="flex justify-between text-sm">
            <span className="text-muted-foreground">Items:</span>
            <span className="font-medium">{totals.itemCount}</span>
          </div>
          <div className="flex justify-between text-2xl font-bold border-t pt-2">
            <span>Total:</span>
            <span className="text-primary">{formatPrice(totals.subtotal)}</span>
          </div>
        </div>

        {/* Checkout Button */}
        {onCheckout && (
          <Button
            onClick={onCheckout}
            disabled={isCheckoutDisabled || items.length === 0}
            size="lg"
            className="w-full text-lg h-14"
          >
            COBRAR
          </Button>
        )}
      </CardFooter>
    </Card>
  );
}

