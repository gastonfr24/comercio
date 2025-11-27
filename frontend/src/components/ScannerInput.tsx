"use client";

import React, { useState, useRef, useEffect } from "react";
import { Search, Loader2, X } from "lucide-react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";

interface ScannerInputProps {
  // eslint-disable-next-line no-unused-vars
  onSearch: (query: string) => void;
  isLoading?: boolean;
  error?: string | null;
  placeholder?: string;
  autoFocus?: boolean;
  onClear?: () => void;
}

/**
 * ScannerInput component for POS system.
 *
 * Optimized input for scanning barcodes or typing product names.
 * Features auto-focus, enter key detection, and visual feedback.
 *
 * @param onSearch - Callback fired when user presses Enter or clicks search
 * @param isLoading - Shows loading spinner when true
 * @param error - Error message to display
 * @param placeholder - Input placeholder text
 * @param autoFocus - Auto-focus input on mount (default: true)
 * @param onClear - Callback fired when user clears the input
 */
export function ScannerInput({
  onSearch,
  isLoading = false,
  error = null,
  placeholder = "Escanear o buscar producto...",
  autoFocus = true,
  onClear,
}: ScannerInputProps) {
  const [query, setQuery] = useState("");
  const inputRef = useRef<HTMLInputElement>(null);

  // Auto-focus on mount
  useEffect(() => {
    if (autoFocus && inputRef.current) {
      inputRef.current.focus();
    }
  }, [autoFocus]);

  /**
   * Handle form submission.
   * Triggers search when user presses Enter or clicks search button.
   */
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const trimmedQuery = query.trim();
    if (trimmedQuery) {
      onSearch(trimmedQuery);
    }
  };

  /**
   * Handle input change.
   * Updates query state and clears error if present.
   */
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setQuery(e.target.value);
  };

  /**
   * Handle clear button click.
   * Clears input and refocuses.
   */
  const handleClear = () => {
    setQuery("");
    if (inputRef.current) {
      inputRef.current.focus();
    }
    if (onClear) {
      onClear();
    }
  };

  return (
    <div className="w-full space-y-2">
      <form onSubmit={handleSubmit} className="relative flex gap-2">
        <div className="relative flex-1">
          <Search className="absolute left-3 top-1/2 h-5 w-5 -translate-y-1/2 text-muted-foreground" />
          <Input
            ref={inputRef}
            type="text"
            value={query}
            onChange={handleChange}
            placeholder={placeholder}
            disabled={isLoading}
            className="pl-10 pr-10 h-12 text-lg"
            aria-label="Buscar producto"
            aria-invalid={!!error}
            aria-describedby={error ? "scanner-error" : undefined}
          />
          {query && !isLoading && (
            <Button
              type="button"
              variant="ghost"
              size="sm"
              onClick={handleClear}
              className="absolute right-2 top-1/2 h-7 w-7 -translate-y-1/2 p-0"
              aria-label="Limpiar búsqueda"
            >
              <X className="h-4 w-4" />
            </Button>
          )}
          {isLoading && (
            <div className="absolute right-3 top-1/2 -translate-y-1/2">
              <Loader2 className="h-5 w-5 animate-spin text-muted-foreground" />
            </div>
          )}
        </div>
        <Button
          type="submit"
          size="lg"
          disabled={isLoading || !query.trim()}
          className="px-6"
        >
          {isLoading ? (
            <>
              <Loader2 className="mr-2 h-5 w-5 animate-spin" />
              Buscando...
            </>
          ) : (
            <>
              <Search className="mr-2 h-5 w-5" />
              Buscar
            </>
          )}
        </Button>
      </form>

      {error && (
        <div
          id="scanner-error"
          className="text-sm text-destructive flex items-center gap-2 px-3 py-2 bg-destructive/10 rounded-md"
          role="alert"
        >
          <span className="font-medium">Error:</span>
          <span>{error}</span>
        </div>
      )}

      <div className="text-xs text-muted-foreground px-1">
        Presiona <kbd className="px-2 py-0.5 bg-muted rounded">Enter</kbd> o
        escanea un código de barras
      </div>
    </div>
  );
}

