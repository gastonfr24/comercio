# 🤝 Guía de Contribución

¡Gracias por tu interés en contribuir al proyecto Comercio! Esta guía te ayudará a hacer contribuciones efectivas.

## 📋 Tabla de Contenidos

- [Código de Conducta](#código-de-conducta)
- [¿Cómo puedo contribuir?](#cómo-puedo-contribuir)
- [Proceso de Desarrollo](#proceso-de-desarrollo)
- [Estándares de Código](#estándares-de-código)
- [Proceso de Pull Request](#proceso-de-pull-request)
- [Reportar Bugs](#reportar-bugs)
- [Sugerir Mejoras](#sugerir-mejoras)

## 📜 Código de Conducta

Este proyecto adhiere a un [Código de Conducta](./CODE_OF_CONDUCT.md). Al participar, se espera que lo cumplas.

## 🎯 ¿Cómo puedo contribuir?

### 1. Reportar Bugs 🐛

Si encuentras un bug:

1. **Verifica** que no exista un issue similar
2. **Crea un issue** usando la plantilla de bug report
3. **Incluye**:
   - Descripción clara del problema
   - Pasos para reproducir
   - Comportamiento esperado vs actual
   - Screenshots si es relevante
   - Versión del sistema y navegador

### 2. Sugerir Features ✨

Para nuevas funcionalidades:

1. **Crea un issue** usando la plantilla de feature request
2. **Describe** claramente el problema que resuelve
3. **Propón** una solución si tienes ideas
4. **Discute** con el equipo antes de implementar

### 3. Contribuir con Código 💻

Ver [Proceso de Desarrollo](#proceso-de-desarrollo) más abajo.

### 4. Mejorar Documentación 📝

La documentación siempre puede mejorar:

- Corregir typos
- Clarificar instrucciones confusas
- Agregar ejemplos
- Actualizar información obsoleta

## 🔄 Proceso de Desarrollo

### 1. Fork y Clone

```bash
# Fork el repositorio en GitHub
# Luego clona tu fork
git clone https://github.com/TU-USUARIO/comercio.git
cd comercio

# Agrega el repositorio original como upstream
git remote add upstream https://github.com/gastonfr24/comercio.git
```

### 2. Crear una Rama

Seguimos **Git Flow**. Lee `.cursorrules` para detalles completos.

```bash
# Actualiza dev
git checkout dev
git pull upstream dev

# Crea tu rama según el tipo de cambio
# Features
git checkout -b feature/sprint1-001-descripcion

# Bugfixes
git checkout -b bugfix/descripcion-del-bug

# Hotfixes (solo desde main)
git checkout main
git checkout -b hotfix/v1.0.1-descripcion
```

### 3. Configurar Entorno

```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate

# Frontend (nueva terminal)
cd frontend
npm install
```

### 4. Hacer Cambios

- **Escribe código limpio** siguiendo los estándares
- **Agrega tests** para nuevas funcionalidades
- **Actualiza documentación** si es necesario
- **Sigue Conventional Commits** para mensajes

### 5. Tests y Linting

```bash
# Backend
cd backend
pytest
flake8 .
black .
isort .

# Frontend
cd frontend
npm run lint
npx prettier --write .
```

### 6. Commit

**IMPORTANTE:** Seguir [Conventional Commits](https://www.conventionalcommits.org/)

```bash
# Buenos ejemplos
git commit -m "feat(auth): add JWT authentication"
git commit -m "fix(cart): resolve decimal precision error"
git commit -m "docs(api): add products endpoint documentation"

# Malos ejemplos (NO HACER)
git commit -m "changes"
git commit -m "fixed bug"
git commit -m "WIP"
```

Ver `.cursorrules` para más detalles sobre commits.

### 7. Push y Pull Request

```bash
# Push a tu fork
git push origin feature/sprint1-001-descripcion

# Crea Pull Request en GitHub hacia 'dev'
```

## 📐 Estándares de Código

### Backend (Python/Django)

```python
# ✅ Bueno
from typing import List, Optional
from django.db import models

class Product(models.Model):
    """
    Modelo para productos en el catálogo.
    
    Attributes:
        name: Nombre del producto
        price: Precio en USD
    """
    name: str = models.CharField(max_length=200)
    price: Decimal = models.DecimalField(max_digits=10, decimal_places=2)
    
    def calculate_discount(self, percentage: float) -> Decimal:
        """Calcula el precio con descuento aplicado."""
        return self.price * (1 - percentage / 100)
```

**Reglas:**
- Usar type hints
- Docstrings en español
- Nombres descriptivos
- Máximo 120 caracteres por línea
- Formatear con Black
- Ordenar imports con isort

### Frontend (TypeScript/React)

```typescript
// ✅ Bueno
interface ProductCardProps {
  product: Product
  onAddToCart: (productId: string) => void
}

export function ProductCard({ product, onAddToCart }: ProductCardProps) {
  const [isLoading, setIsLoading] = useState(false)
  
  const handleClick = async () => {
    setIsLoading(true)
    try {
      await onAddToCart(product.id)
    } finally {
      setIsLoading(false)
    }
  }
  
  return (
    <Card>
      <CardHeader>
        <CardTitle>{product.name}</CardTitle>
      </CardHeader>
      <CardContent>
        <Button onClick={handleClick} disabled={isLoading}>
          Agregar al carrito
        </Button>
      </CardContent>
    </Card>
  )
}
```

**Reglas:**
- Usar TypeScript estricto
- Interfaces para props
- Componentes funcionales con hooks
- Nombres descriptivos
- Máximo 100 caracteres por línea
- Formatear con Prettier

## 🔍 Proceso de Pull Request

### Template de PR

```markdown
## 📋 Descripción

[Descripción clara de los cambios]

## 🔗 Issue Relacionado

Closes #123

## 🎯 Tipo de Cambio

- [ ] 🐛 Bug fix
- [ ] ✨ Nueva feature
- [ ] 💥 Breaking change
- [ ] 📝 Documentación

## ✅ Checklist

- [ ] Código sigue estándares del proyecto
- [ ] Auto-revisión realizada
- [ ] Código comentado en áreas complejas
- [ ] Documentación actualizada
- [ ] Sin warnings nuevos
- [ ] Tests agregados/actualizados
- [ ] Tests pasan localmente
- [ ] CHANGELOG.md actualizado

## 🧪 Testing

[Describe las pruebas realizadas]

## 📸 Screenshots

[Si aplica]
```

### Proceso de Revisión

1. **Crear PR** hacia `dev` (no a `main` directamente)
2. **Asignar reviewers** (al menos 1)
3. **CI/CD** debe pasar (cuando esté configurado)
4. **Resolver comentarios** del reviewer
5. **Aprobar y merge** por el reviewer
6. **Squash merge** para mantener historial limpio
7. **Eliminar rama** después del merge

### Criterios de Aprobación

Un PR será aprobado si:

- ✅ Sigue los estándares de código
- ✅ Tiene tests apropiados
- ✅ Documentación está actualizada
- ✅ CHANGELOG.md está actualizado
- ✅ Commits siguen Conventional Commits
- ✅ No introduce regresiones
- ✅ CI/CD pasa (cuando esté configurado)

## 🐛 Reportar Bugs

### Template de Bug Report

```markdown
## 🐛 Descripción del Bug

[Descripción clara y concisa]

## 📋 Pasos para Reproducir

1. Ir a '...'
2. Click en '...'
3. Scroll hasta '...'
4. Ver error

## ✅ Comportamiento Esperado

[Qué debería suceder]

## ❌ Comportamiento Actual

[Qué sucede actualmente]

## 📸 Screenshots

[Si es relevante]

## 🖥️ Entorno

- OS: [e.g. Windows 11, macOS 13, Ubuntu 22.04]
- Navegador: [e.g. Chrome 120, Firefox 121]
- Versión: [e.g. v1.0.0]

## 📝 Contexto Adicional

[Cualquier información adicional]
```

## ✨ Sugerir Mejoras

### Template de Feature Request

```markdown
## 🎯 ¿Qué problema resuelve?

[Descripción del problema o necesidad]

## 💡 Solución Propuesta

[Cómo propones resolverlo]

## 🔄 Alternativas Consideradas

[Otras soluciones que consideraste]

## 📊 Impacto

- **Usuarios afectados:** [e.g. todos, solo admin]
- **Prioridad:** [Alta/Media/Baja]
- **Complejidad estimada:** [Alta/Media/Baja]

## 📝 Contexto Adicional

[Cualquier información adicional]
```

## 🎨 Estilo de Código

### Python

```bash
# Formateo automático
black .
isort .

# Verificación
flake8 .
mypy .
```

### TypeScript/React

```bash
# Formateo automático
npx prettier --write .

# Verificación
npm run lint
```

## 📝 Documentación

Al actualizar documentación:

1. **Mantén consistencia** con el estilo existente
2. **Usa emojis** para mejorar legibilidad
3. **Incluye ejemplos** de código cuando sea posible
4. **Actualiza índices** si agregas nuevos archivos
5. **Verifica enlaces** funcionan correctamente

## 🤔 ¿Preguntas?

- **Dudas sobre código**: Crea un issue con la etiqueta `question`
- **Propuestas de arquitectura**: Crea un ADR en `docs/decisions/`
- **Problemas de setup**: Ver [Troubleshooting](./guides/troubleshooting.md)

## 📞 Contacto

- **GitHub Issues**: Para bugs y features
- **GitHub Discussions**: Para preguntas generales
- **Email**: Para temas privados o sensibles

## 🙏 Agradecimientos

¡Gracias por contribuir al proyecto! Tu ayuda es muy apreciada.

---

**Última actualización:** 2025-01-XX  
**Mantenedores:** @gastonfr24

