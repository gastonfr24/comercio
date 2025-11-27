"use client";

import { useState } from "react";
import { ScannerInput } from "@/components/ScannerInput";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

/**
 * POS page for testing ScannerInput component.
 */
export default function POSPage() {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [searchHistory, setSearchHistory] = useState<string[]>([]);

  /**
   * Handle search submission.
   */
  const handleSearch = async (query: string) => {
    setIsLoading(true);
    setError(null);

    try {
      // Simulate API call
      await new Promise((resolve) => setTimeout(resolve, 500));

      // Add to history
      setSearchHistory((prev) => [query, ...prev].slice(0, 10));
    } catch (err) {
      setError("Error al buscar producto");
    } finally {
      setIsLoading(false);
    }
  };

  /**
   * Handle clear action.
   */
  const handleClear = () => {
    setError(null);
  };

  return (
    <div className="container mx-auto p-6 max-w-4xl">
      <h1 className="text-3xl font-bold mb-6">Punto de Venta (POS)</h1>

      <div className="space-y-6">
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

        {searchHistory.length > 0 && (
          <Card>
            <CardHeader>
              <CardTitle>Historial de Búsquedas</CardTitle>
            </CardHeader>
            <CardContent>
              <ul className="space-y-2">
                {searchHistory.map((query, index) => (
                  <li
                    key={index}
                    className="p-2 bg-muted rounded text-sm flex items-center gap-2"
                  >
                    <span className="text-muted-foreground">#{index + 1}</span>
                    <span className="font-medium">{query}</span>
                  </li>
                ))}
              </ul>
            </CardContent>
          </Card>
        )}
      </div>
    </div>
  );
}

