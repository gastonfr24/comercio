# Frontend - Next.js con Tailwind CSS y shadcn/ui

Este es el frontend del proyecto de comercio, construido con Next.js 14, TypeScript, Tailwind CSS y shadcn/ui.

## Requisitos

- Node.js 18+
- npm o yarn

## Instalación

1. Instalar dependencias:
```bash
npm install
# o
yarn install
```

2. Configurar variables de entorno:
```bash
# Copiar el archivo de ejemplo
copy .env.local.example .env.local

# Editar .env.local con tus configuraciones
```

3. Ejecutar el servidor de desarrollo:
```bash
npm run dev
# o
yarn dev
```

4. Abrir [http://localhost:3000](http://localhost:3000) en tu navegador.

## Scripts disponibles

```bash
# Ejecutar en modo desarrollo
npm run dev

# Construir para producción
npm run build

# Ejecutar en modo producción (requiere build primero)
npm run start

# Ejecutar linter
npm run lint
```

## Estructura del proyecto

```
frontend/
├── src/
│   ├── app/              # App Router de Next.js 14
│   │   ├── layout.tsx   # Layout principal
│   │   ├── page.tsx     # Página principal
│   │   └── globals.css  # Estilos globales + Tailwind
│   ├── components/      # Componentes React
│   │   └── ui/         # Componentes de shadcn/ui
│   │       ├── button.tsx
│   │       ├── card.tsx
│   │       └── badge.tsx
│   └── lib/            # Utilidades y configuraciones
│       ├── api.ts      # Cliente API con Axios
│       └── utils.ts    # Utilidad cn() para Tailwind
├── public/             # Archivos estáticos
├── components.json     # Configuración de shadcn/ui
├── tailwind.config.ts  # Configuración de Tailwind CSS
├── postcss.config.js   # Configuración de PostCSS
├── next.config.js      # Configuración de Next.js
├── tsconfig.json       # Configuración de TypeScript
└── package.json        # Dependencias y scripts
```

## Stack de tecnologías

### Framework y Lenguaje
- ✅ **Next.js 14** - Framework React con App Router
- ✅ **TypeScript** - Tipado estático
- ✅ **React 18** - Biblioteca de UI

### Estilos
- ✅ **Tailwind CSS** - Framework CSS utility-first
- ✅ **shadcn/ui** - Componentes de UI accesibles y customizables
- ✅ **Lucide React** - Iconos modernos

### Utilities
- ✅ **class-variance-authority (cva)** - Variantes de componentes
- ✅ **clsx** - Utilidad para clases condicionales
- ✅ **tailwind-merge** - Merge de clases Tailwind
- ✅ **Radix UI** - Primitivas de UI accesibles

### API
- ✅ **Axios** - Cliente HTTP configurado

## Componentes de shadcn/ui incluidos

El proyecto incluye los siguientes componentes base:

- **Button** - Botones con múltiples variantes
- **Card** - Tarjetas con header, content y footer
- **Badge** - Badges/etiquetas con variantes

### Agregar más componentes

Para agregar más componentes de shadcn/ui:

```bash
npx shadcn-ui@latest add <component-name>

# Ejemplos:
npx shadcn-ui@latest add dialog
npx shadcn-ui@latest add dropdown-menu
npx shadcn-ui@latest add input
npx shadcn-ui@latest add form
npx shadcn-ui@latest add table
```

## Utilidad cn()

El proyecto incluye la utilidad `cn()` en `src/lib/utils.ts` para combinar clases de Tailwind:

```typescript
import { cn } from '@/lib/utils'

<div className={cn(
  'base-classes',
  condition && 'conditional-classes',
  className
)} />
```

## Tailwind CSS

### Tema personalizado

El proyecto está configurado con variables CSS para temas claros y oscuros en `globals.css`.

### Clases útiles

```typescript
// Responsive
<div className="hidden md:block lg:flex" />

// Spacing
<div className="p-4 mx-auto space-y-4" />

// Gradients
<div className="bg-gradient-to-r from-purple-600 to-indigo-600" />

// Hover y estados
<button className="hover:bg-primary/90 focus:ring-2" />
```

## Conexión con el Backend

El frontend está configurado para conectarse con el backend Django en `http://localhost:8000/api`.

Configuración en `.env.local`:
```env
API_URL=http://localhost:8000/api
```

## Formateo y Linting

```bash
# ESLint
npm run lint

# Prettier (con plugin de Tailwind)
npx prettier --write .

# El formateo automático está configurado en VSCode
```

## Próximos pasos

1. Crear más páginas en `src/app/`
2. Agregar más componentes de shadcn/ui según necesites
3. Implementar autenticación con contexto
4. Crear layouts compartidos
5. Agregar gestión de estado (Zustand, Context API, etc.)
6. Implementar rutas protegidas
7. Agregar modo oscuro (dark mode)

## Recursos

- [Next.js Docs](https://nextjs.org/docs)
- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [shadcn/ui Docs](https://ui.shadcn.com)
- [Radix UI Docs](https://www.radix-ui.com)
- [Lucide Icons](https://lucide.dev)
