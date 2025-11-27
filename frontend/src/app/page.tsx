'use client'

import { useEffect, useState } from 'react'
import { useRouter } from 'next/navigation'
import { checkApiHealth } from '@/lib/api'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { CheckCircle2, XCircle, Palette, Rocket, BookOpen, Target } from 'lucide-react'

export default function Home() {
  const router = useRouter()
  const [apiStatus, setApiStatus] = useState<{
    status: 'loading' | 'success' | 'error'
    message: string
  }>({
    status: 'loading',
    message: 'Verificando conexión...',
  })

  useEffect(() => {
    const checkApi = async () => {
      try {
        const response = await checkApiHealth()
        setApiStatus({
          status: 'success',
          message: response.message,
        })
      } catch (error) {
        setApiStatus({
          status: 'error',
          message: 'No se pudo conectar con la API',
        })
      }
    }

    checkApi()
  }, [])

  /**
   * Navigate to POS page.
   */
  const handleGoToPOS = () => {
    router.push('/pos')
  }

  /**
   * Navigate to API documentation.
   */
  const handleGoToAPI = () => {
    window.open('http://localhost:8000/api/', '_blank')
  }

  return (
    <main className="min-h-screen bg-gradient-to-br from-purple-600 via-purple-700 to-indigo-800">
      <div className="container mx-auto px-4 py-16">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-5xl md:text-7xl font-extrabold text-white mb-4">
            Bienvenido a{' '}
            <span className="bg-gradient-to-r from-yellow-400 to-orange-500 bg-clip-text text-transparent">
              Comercio
            </span>
          </h1>
          <p className="text-xl text-purple-100 mb-6">
            Plataforma de e-commerce construida con Next.js y Django
          </p>
          <div className="flex flex-wrap gap-2 justify-center">
            <Badge variant="secondary" className="text-sm py-1">
              Next.js 14
            </Badge>
            <Badge variant="secondary" className="text-sm py-1">
              Django REST
            </Badge>
            <Badge variant="secondary" className="text-sm py-1">
              Tailwind CSS
            </Badge>
            <Badge variant="secondary" className="text-sm py-1">
              shadcn/ui
            </Badge>
          </div>
        </div>

        {/* API Status Card */}
        <Card className="mb-12 max-w-2xl mx-auto border-purple-200 shadow-2xl">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              {apiStatus.status === 'loading' && (
                <div className="h-5 w-5 animate-spin rounded-full border-2 border-primary border-t-transparent" />
              )}
              {apiStatus.status === 'success' && (
                <CheckCircle2 className="h-5 w-5 text-green-600" />
              )}
              {apiStatus.status === 'error' && (
                <XCircle className="h-5 w-5 text-red-600" />
              )}
              Estado de la API
            </CardTitle>
            <CardDescription>Conexión con el backend Django</CardDescription>
          </CardHeader>
          <CardContent>
            <p
              className={`text-lg font-medium ${
                apiStatus.status === 'success'
                  ? 'text-green-600'
                  : apiStatus.status === 'error'
                  ? 'text-red-600'
                  : 'text-gray-600'
              }`}
            >
              {apiStatus.message}
            </p>
          </CardContent>
        </Card>

        {/* Features Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
          <Card className="hover:shadow-xl transition-shadow duration-300 border-purple-200">
            <CardHeader>
              <div className="h-12 w-12 rounded-lg bg-gradient-to-br from-pink-500 to-purple-600 flex items-center justify-center mb-2">
                <Palette className="h-6 w-6 text-white" />
              </div>
              <CardTitle>Frontend Moderno</CardTitle>
            </CardHeader>
            <CardContent>
              <ul className="space-y-1 text-sm text-muted-foreground">
                <li>✓ Next.js 14 con App Router</li>
                <li>✓ TypeScript</li>
                <li>✓ Tailwind CSS</li>
                <li>✓ shadcn/ui</li>
              </ul>
            </CardContent>
          </Card>

          <Card className="hover:shadow-xl transition-shadow duration-300 border-purple-200">
            <CardHeader>
              <div className="h-12 w-12 rounded-lg bg-gradient-to-br from-blue-500 to-cyan-600 flex items-center justify-center mb-2">
                <Rocket className="h-6 w-6 text-white" />
              </div>
              <CardTitle>Backend Robusto</CardTitle>
            </CardHeader>
            <CardContent>
              <ul className="space-y-1 text-sm text-muted-foreground">
                <li>✓ Django REST Framework</li>
                <li>✓ API RESTful</li>
                <li>✓ PostgreSQL ready</li>
                <li>✓ Docker support</li>
              </ul>
            </CardContent>
          </Card>

          <Card className="hover:shadow-xl transition-shadow duration-300 border-purple-200">
            <CardHeader>
              <div className="h-12 w-12 rounded-lg bg-gradient-to-br from-green-500 to-emerald-600 flex items-center justify-center mb-2">
                <BookOpen className="h-6 w-6 text-white" />
              </div>
              <CardTitle>Documentación</CardTitle>
            </CardHeader>
            <CardContent>
              <ul className="space-y-1 text-sm text-muted-foreground">
                <li>✓ README completo</li>
                <li>✓ Guía de setup</li>
                <li>✓ Docker compose</li>
                <li>✓ Best practices</li>
              </ul>
            </CardContent>
          </Card>

          <Card className="hover:shadow-xl transition-shadow duration-300 border-purple-200">
            <CardHeader>
              <div className="h-12 w-12 rounded-lg bg-gradient-to-br from-orange-500 to-red-600 flex items-center justify-center mb-2">
                <Target className="h-6 w-6 text-white" />
              </div>
              <CardTitle>Empezar</CardTitle>
            </CardHeader>
            <CardContent>
              <ul className="space-y-1 text-sm text-muted-foreground">
                <li>→ Backend: :8000</li>
                <li>→ Frontend: :3000</li>
                <li>→ Admin: :8000/admin</li>
                <li>→ API: :8000/api</li>
              </ul>
            </CardContent>
          </Card>
        </div>

        {/* CTA Section */}
        <div className="text-center">
          <Card className="inline-block border-purple-200 shadow-2xl">
            <CardHeader>
              <CardTitle className="text-2xl">¿Listo para comenzar?</CardTitle>
              <CardDescription>
                Revisa la documentación para configurar tu entorno de desarrollo
              </CardDescription>
            </CardHeader>
            <CardContent className="flex flex-col sm:flex-row gap-4 justify-center">
              <Button 
                size="lg" 
                onClick={handleGoToPOS}
                className="bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700"
              >
                Ir al POS
              </Button>
              <Button 
                size="lg" 
                variant="outline"
                onClick={handleGoToAPI}
              >
                Explorar API
              </Button>
            </CardContent>
          </Card>
        </div>
      </div>
    </main>
  )
}

