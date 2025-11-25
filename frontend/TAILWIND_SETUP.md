# 🎨 Configuración de Tailwind CSS y shadcn/ui

Este documento detalla la configuración de Tailwind CSS y shadcn/ui en el proyecto.

## ✅ Lo que ya está configurado

### Dependencias instaladas

```json
// Dependencias de producción
"@radix-ui/react-slot": "^1.0.2"
"class-variance-authority": "^0.7.0"
"clsx": "^2.1.0"
"tailwind-merge": "^2.2.0"
"tailwindcss-animate": "^1.0.7"
"lucide-react": "^0.303.0"

// Dependencias de desarrollo
"tailwindcss": "^3.4.0"
"postcss": "^8.4.32"
"autoprefixer": "^10.4.16"
"prettier-plugin-tailwindcss": "^0.5.10"
```

### Archivos de configuración

- ✅ `tailwind.config.ts` - Configuración completa de Tailwind
- ✅ `postcss.config.js` - Configuración de PostCSS
- ✅ `components.json` - Configuración de shadcn/ui
- ✅ `src/app/globals.css` - Estilos globales con directivas Tailwind
- ✅ `src/lib/utils.ts` - Utilidad `cn()` para merge de clases

### Componentes UI incluidos

- ✅ `Button` - Botones con múltiples variantes
- ✅ `Card` - Tarjetas con subcomponentes
- ✅ `Badge` - Etiquetas/badges con variantes

## 🚀 Instalación

1. **Instalar dependencias:**

```bash
cd frontend
npm install
```

2. **Verificar instalación:**

```bash
npm run dev
```

Abre http://localhost:3000 y deberías ver la página de inicio con componentes estilizados.

## 📦 Agregar más componentes de shadcn/ui

shadcn/ui ofrece muchos componentes. Para agregar más:

```bash
# Comando general
npx shadcn-ui@latest add [component-name]

# Ejemplos de componentes útiles:
npx shadcn-ui@latest add dialog
npx shadcn-ui@latest add dropdown-menu
npx shadcn-ui@latest add input
npx shadcn-ui@latest add form
npx shadcn-ui@latest add table
npx shadcn-ui@latest add select
npx shadcn-ui@latest add checkbox
npx shadcn-ui@latest add radio-group
npx shadcn-ui@latest add switch
npx shadcn-ui@latest add tabs
npx shadcn-ui@latest add toast
npx shadcn-ui@latest add sheet
npx shadcn-ui@latest add alert
npx shadcn-ui@latest add avatar
npx shadcn-ui@latest add calendar
npx shadcn-ui@latest add command
```

Cada comando descargará el componente en `src/components/ui/`.

## 🎨 Uso de componentes

### Button

```tsx
import { Button } from '@/components/ui/button'

// Variantes
<Button>Default</Button>
<Button variant="destructive">Destructive</Button>
<Button variant="outline">Outline</Button>
<Button variant="secondary">Secondary</Button>
<Button variant="ghost">Ghost</Button>
<Button variant="link">Link</Button>

// Tamaños
<Button size="sm">Small</Button>
<Button size="default">Default</Button>
<Button size="lg">Large</Button>
<Button size="icon">🚀</Button>
```

### Card

```tsx
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from '@/components/ui/card'

<Card>
  <CardHeader>
    <CardTitle>Título</CardTitle>
    <CardDescription>Descripción</CardDescription>
  </CardHeader>
  <CardContent>
    <p>Contenido de la tarjeta</p>
  </CardContent>
  <CardFooter>
    <Button>Acción</Button>
  </CardFooter>
</Card>
```

### Badge

```tsx
import { Badge } from '@/components/ui/badge'

<Badge>Default</Badge>
<Badge variant="secondary">Secondary</Badge>
<Badge variant="destructive">Destructive</Badge>
<Badge variant="outline">Outline</Badge>
```

## 🎯 Utilidad cn()

Combina clases de Tailwind de forma inteligente:

```tsx
import { cn } from '@/lib/utils'

function MyComponent({ className, isActive }) {
  return (
    <div className={cn(
      'p-4 rounded-lg',           // Clases base
      isActive && 'bg-blue-500',  // Clases condicionales
      className                    // Clases del padre
    )} />
  )
}
```

## 🌈 Sistema de colores

El proyecto usa variables CSS para temas:

```css
/* En globals.css */
:root {
  --primary: 222.2 47.4% 11.2%;
  --secondary: 210 40% 96.1%;
  --accent: 210 40% 96.1%;
  --destructive: 0 84.2% 60.2%;
  /* ... más colores */
}
```

Usar en Tailwind:

```tsx
<div className="bg-primary text-primary-foreground">
<div className="bg-secondary text-secondary-foreground">
<div className="bg-destructive text-destructive-foreground">
```

## 🌙 Dark Mode (próximamente)

Para habilitar modo oscuro:

1. **Instalar next-themes:**
```bash
npm install next-themes
```

2. **Crear ThemeProvider:**
```tsx
// src/components/theme-provider.tsx
'use client'

import { ThemeProvider as NextThemesProvider } from 'next-themes'

export function ThemeProvider({ children, ...props }) {
  return <NextThemesProvider {...props}>{children}</NextThemesProvider>
}
```

3. **Envolver en layout.tsx:**
```tsx
import { ThemeProvider } from '@/components/theme-provider'

export default function RootLayout({ children }) {
  return (
    <html lang="es" suppressHydrationWarning>
      <body>
        <ThemeProvider attribute="class" defaultTheme="system" enableSystem>
          {children}
        </ThemeProvider>
      </body>
    </html>
  )
}
```

4. **Toggle de tema:**
```tsx
import { useTheme } from 'next-themes'

function ThemeToggle() {
  const { setTheme } = useTheme()
  
  return (
    <Button onClick={() => setTheme('dark')}>Dark</Button>
  )
}
```

## 📱 Responsive Design

Tailwind usa breakpoints mobile-first:

```tsx
<div className="
  p-2              /* móvil */
  md:p-4           /* tablet */
  lg:p-8           /* desktop */
  xl:p-12          /* pantallas grandes */
">
```

Breakpoints:
- `sm`: 640px
- `md`: 768px
- `lg`: 1024px
- `xl`: 1280px
- `2xl`: 1536px

## 🎨 Clases Tailwind útiles

### Layout
```tsx
<div className="flex flex-col md:flex-row gap-4">
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
<div className="container mx-auto px-4">
```

### Spacing
```tsx
<div className="p-4 m-2 space-y-4">
<div className="px-6 py-4">
```

### Colores y Backgrounds
```tsx
<div className="bg-gradient-to-r from-purple-600 to-indigo-600">
<div className="bg-white dark:bg-gray-900">
<p className="text-gray-600 dark:text-gray-300">
```

### Efectos y Transiciones
```tsx
<div className="hover:shadow-xl transition-shadow duration-300">
<button className="hover:scale-105 transform transition-transform">
<div className="opacity-0 hover:opacity-100 transition-opacity">
```

### Bordes y Sombras
```tsx
<div className="border border-gray-200 rounded-lg shadow-sm">
<div className="shadow-md hover:shadow-lg">
```

## 🔍 IntelliSense de Tailwind

Para autocompletado en VSCode, instala:

```bash
# Extensión recomendada
Tailwind CSS IntelliSense
```

La configuración en `.vscode/settings.json` ya incluye soporte para:
- Clases dentro de `cn()`
- Clases dentro de `cva()`

## 📝 Formateo automático

Prettier está configurado para ordenar clases de Tailwind automáticamente:

```bash
# Formatear todos los archivos
npx prettier --write .

# O formateo automático al guardar (VSCode)
```

## 🎓 Recursos de aprendizaje

- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [shadcn/ui Components](https://ui.shadcn.com/docs/components)
- [Radix UI Primitives](https://www.radix-ui.com/primitives)
- [Lucide Icons](https://lucide.dev/icons/)
- [Tailwind Cheat Sheet](https://nerdcave.com/tailwind-cheat-sheet)

## 🛠️ Troubleshooting

### Estilos no se aplican

```bash
# Limpiar caché
rm -rf .next
npm run dev
```

### Clases Tailwind no funcionan

Verifica que el archivo esté incluido en `tailwind.config.ts`:

```ts
content: [
  './src/**/*.{ts,tsx}',  // Debe incluir tu archivo
]
```

### IntelliSense no funciona

1. Reinstala extensión Tailwind CSS IntelliSense
2. Recarga VSCode: `Ctrl+Shift+P` → "Reload Window"

## ✨ Próximos pasos

1. Agregar más componentes según necesites
2. Implementar dark mode
3. Crear componentes custom basados en shadcn/ui
4. Configurar tema personalizado en `tailwind.config.ts`
5. Explorar plugins de Tailwind adicionales

¡Feliz desarrollo con Tailwind y shadcn/ui! 🎨✨

