"use client";

import { useState } from "react";
import { ScannerInput } from "@/components/ScannerInput";
import { ProductList, Product } from "@/components/ProductList";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { searchProducts } from "@/lib/api";

/**
 * POS page for point of sale operations.
 */
export default function POSPage() {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [products, setProducts] = useState<Product[]>([]);
  const [hasSearched, setHasSearched] = useState(false);

  /**
   * Handle search submission.
   * Calls API to search for products.
   */
  const handleSearch = async (query: string) => {
    setIsLoading(true);
    setError(null);
    setHasSearched(true);

    try {
      const results = await searchProducts(query);
      setProducts(results);

      if (results.length === 0) {
        setError("No se encontraron productos");
      }
    } catch (err) {
      setError("Error al buscar productos. Intenta nuevamente.");
      setProducts([]);
    } finally {
      setIsLoading(false);
    }
  };

  /**
   * Handle clear action.
   * Resets search results and error state.
   */
  const handleClear = () => {
    setError(null);
    setProducts([]);
    setHasSearched(false);
  };

  /**
   * Handle add to cart.
   * TODO: Implement cart functionality in T-008.
   */
  const handleAddToCart = (product: Product) => {
    // eslint-disable-next-line no-console
    console.log("Adding to cart:", product);
    // TODO: Implement with useCart hook
  };

  return (
    <div className="container mx-auto p-4 md:p-6 max-w-7xl">
      <div className="mb-6">
        <h1 className="text-3xl font-bold mb-2">Punto de Venta</h1>
        <p className="text-muted-foreground">
          Escanea o busca productos para agregarlos al carrito
        </p>
      </div>

      <div className="space-y-6">
        {/* Scanner Section */}
        <Card>
          <CardHeader>
            <CardTitle>Buscar Producto</CardTitle>
          </CardHeader>
          <CardContent>
            <ScannerInput
              onSearch={handleSearch}
              isLoading={isLoading}
              error={error}
              onClear={handleClear}
            />
          </CardContent>
        </Card>

        {/* Results Section */}
        {hasSearched && (
          <Card>
            <CardHeader>
              <CardTitle>
                Resultados
                {products.length > 0 && (
                  <span className="ml-2 text-muted-foreground text-base font-normal">
                    ({products.length} {products.length === 1 ? "producto" : "productos"})
                  </span>
                )}
              </CardTitle>
            </CardHeader>
            <CardContent>
              <ProductList
                products={products}
                onAddToCart={handleAddToCart}
                isLoading={isLoading}
              />
            </CardContent>
          </Card>
        )}

        {/* Info Section */}
        {!hasSearched && (
          <Card className="bg-muted/50">
            <CardContent className="pt-6">
              <div className="text-center text-muted-foreground">
                <p className="text-lg mb-2">👆 Comienza escaneando o buscando un producto</p>
                <p className="text-sm">
                  Usa el lector de código de barras o escribe el nombre del producto
                </p>
              </div>
            </CardContent>
          </Card>
        )}
      </div>
    </div>
  );
}
