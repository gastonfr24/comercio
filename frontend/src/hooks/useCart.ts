"use client";

import { useState, useEffect, useCallback } from "react";

export interface CartItem {
  id: number;
  barcode: string;
  name: string;
  price: number;
  quantity: number;
}

export interface CartTotals {
  subtotal: number;
  itemCount: number;
}

const CART_STORAGE_KEY = "pos-cart";

/**
 * Custom hook for managing shopping cart state.
 *
 * Features:
 * - Add items to cart
 * - Remove items from cart
 * - Update item quantities
 * - Calculate totals
 * - Persist to localStorage
 * - Clear cart
 *
 * @returns Cart state and methods
 */
export function useCart() {
  const [items, setItems] = useState<CartItem[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  /**
   * Load cart from localStorage on mount.
   */
  useEffect(() => {
    try {
      const stored = localStorage.getItem(CART_STORAGE_KEY);
      if (stored) {
        const parsed = JSON.parse(stored);
        setItems(parsed);
      }
    } catch {
      // Silently fail if localStorage is not available
    } finally {
      setIsLoading(false);
    }
  }, []);

  /**
   * Save cart to localStorage whenever it changes.
   */
  useEffect(() => {
    if (!isLoading) {
      try {
        localStorage.setItem(CART_STORAGE_KEY, JSON.stringify(items));
      } catch {
        // Silently fail if localStorage is not available
      }
    }
  }, [items, isLoading]);

  /**
   * Add item to cart or increment quantity if already exists.
   */
  const addItem = useCallback(
    (product: { id: number; barcode: string; name: string; price: number }) => {
      setItems((prevItems) => {
        const existingItem = prevItems.find((item) => item.id === product.id);

        if (existingItem) {
          // Increment quantity if item already exists
          return prevItems.map((item) =>
            item.id === product.id
              ? { ...item, quantity: item.quantity + 1 }
              : item
          );
        } else {
          // Add new item with quantity 1
          return [
            ...prevItems,
            {
              id: product.id,
              barcode: product.barcode,
              name: product.name,
              price: product.price,
              quantity: 1,
            },
          ];
        }
      });
    },
    []
  );

  /**
   * Remove item from cart completely.
   */
  const removeItem = useCallback((productId: number) => {
    setItems((prevItems) => prevItems.filter((item) => item.id !== productId));
  }, []);

  /**
   * Update quantity of an item in cart.
   * If quantity is 0 or less, removes the item.
   */
  const updateQuantity = useCallback((productId: number, quantity: number) => {
    if (quantity <= 0) {
      setItems((prevItems) => prevItems.filter((item) => item.id !== productId));
    } else {
      setItems((prevItems) =>
        prevItems.map((item) =>
          item.id === productId ? { ...item, quantity } : item
        )
      );
    }
  }, []);

  /**
   * Increment item quantity by 1.
   */
  const incrementItem = useCallback((productId: number) => {
    setItems((prevItems) =>
      prevItems.map((item) =>
        item.id === productId ? { ...item, quantity: item.quantity + 1 } : item
      )
    );
  }, []);

  /**
   * Decrement item quantity by 1.
   * If quantity becomes 0, removes the item.
   */
  const decrementItem = useCallback((productId: number) => {
    setItems((prevItems) => {
      return prevItems
        .map((item) => {
          if (item.id === productId) {
            const newQuantity = item.quantity - 1;
            return newQuantity > 0 ? { ...item, quantity: newQuantity } : null;
          }
          return item;
        })
        .filter((item): item is CartItem => item !== null);
    });
  }, []);

  /**
   * Clear all items from cart.
   */
  const clearCart = useCallback(() => {
    setItems([]);
  }, []);

  /**
   * Calculate cart totals.
   */
  const totals: CartTotals = {
    subtotal: items.reduce((sum, item) => sum + item.price * item.quantity, 0),
    itemCount: items.reduce((sum, item) => sum + item.quantity, 0),
  };

  /**
   * Check if a product is in the cart.
   */
  const isInCart = useCallback(
    (productId: number): boolean => {
      return items.some((item) => item.id === productId);
    },
    [items]
  );

  /**
   * Get quantity of a specific product in cart.
   */
  const getItemQuantity = useCallback(
    (productId: number): number => {
      const item = items.find((item) => item.id === productId);
      return item?.quantity || 0;
    },
    [items]
  );

  return {
    items,
    totals,
    isLoading,
    addItem,
    removeItem,
    updateQuantity,
    incrementItem,
    decrementItem,
    clearCart,
    isInCart,
    getItemQuantity,
  };
}

