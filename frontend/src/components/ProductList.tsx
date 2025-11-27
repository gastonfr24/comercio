"use client";

import React from "react";
import { Plus, Package } from "lucide-react";
import { Card, CardContent, CardFooter, CardHeader } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";

export interface Product {
  id: number;
  barcode: string;
  name: string;
  price: number;
  stock: number;
  category?: string;
  is_active: boolean;
  in_stock: boolean;
}

interface ProductListProps {
  products: Product[];
  // eslint-disable-next-line no-unused-vars
  onAddToCart: (product: Product) => void;
  isLoading?: boolean;
}

/**
 * ProductList component for displaying search results.
 *
 * Shows products in a responsive grid with add to cart functionality.
 * Optimized for POS quick selection.
 *
 * @param products - Array of products to display
 * @param onAddToCart - Callback fired when user clicks add to cart
 * @param isLoading - Shows loading state when true
 */
export function ProductList({
  products,
  onAddToCart,
  isLoading = false,
}: ProductListProps) {
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
   * Handle add to cart click.
   */
  const handleAddClick = (product: Product) => {
    if (product.in_stock && product.is_active) {
      onAddToCart(product);
    }
  };

  // Loading state
  if (isLoading) {
    return (
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
        {[...Array(8)].map((_, index) => (
          <Card key={index} className="animate-pulse">
            <CardHeader className="h-20 bg-muted" />
            <CardContent className="space-y-2 pt-4">
              <div className="h-4 bg-muted rounded" />
              <div className="h-4 bg-muted rounded w-2/3" />
            </CardContent>
            <CardFooter className="h-12 bg-muted" />
          </Card>
        ))}
      </div>
    );
  }

  // Empty state
  if (products.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center py-12 text-center">
        <Package className="h-16 w-16 text-muted-foreground mb-4" />
        <h3 className="text-lg font-semibold mb-2">No se encontraron productos</h3>
        <p className="text-muted-foreground max-w-md">
          Intenta buscar con un código de barras diferente o el nombre del producto.
        </p>
      </div>
    );
  }

  // Products grid
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
      {products.map((product) => (
        <Card
          key={product.id}
          className={`
            transition-all hover:shadow-lg
            ${!product.in_stock || !product.is_active ? "opacity-60" : ""}
          `}
        >
          <CardHeader className="pb-3">
            <div className="flex items-start justify-between gap-2">
              <div className="flex-1 min-w-0">
                <h3 className="font-semibold text-lg leading-tight line-clamp-2">
                  {product.name}
                </h3>
                <p className="text-xs text-muted-foreground mt-1">
                  {product.barcode}
                </p>
              </div>
              {product.category && (
                <Badge variant="outline" className="shrink-0 text-xs">
                  {product.category}
                </Badge>
              )}
            </div>
          </CardHeader>

          <CardContent className="pb-3">
            <div className="flex items-baseline justify-between">
              <div>
                <p className="text-2xl font-bold text-primary">
                  {formatPrice(product.price)}
                </p>
              </div>
              <div className="text-right">
                <p
                  className={`text-sm font-medium ${
                    product.in_stock ? "text-green-600" : "text-red-600"
                  }`}
                >
                  {product.in_stock ? `Stock: ${product.stock}` : "Sin stock"}
                </p>
              </div>
            </div>
          </CardContent>

          <CardFooter className="pt-3">
            <Button
              onClick={() => handleAddClick(product)}
              disabled={!product.in_stock || !product.is_active}
              className="w-full"
              size="lg"
            >
              <Plus className="mr-2 h-5 w-5" />
              Agregar al carrito
            </Button>
          </CardFooter>
        </Card>
      ))}
    </div>
  );
}

