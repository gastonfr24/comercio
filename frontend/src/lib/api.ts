import axios from 'axios'

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'
const API_TIMEOUT = parseInt(process.env.NEXT_PUBLIC_API_TIMEOUT || '30000')

const api = axios.create({
  baseURL: `${API_URL}/api`,
  timeout: API_TIMEOUT,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Interceptor para agregar el token de autenticación si existe
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Interceptor para manejar errores de respuesta
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Manejar token expirado o no autorizado
      localStorage.removeItem('token')
      window.location.href = '/login'
    }
    return Promise.reject(error)
  }
)

// Función para verificar el estado de la API
export const checkApiHealth = async () => {
  const response = await api.get('/health/')
  return response.data
}

/**
 * Search products by query.
 * Searches by barcode (exact) or name (partial).
 *
 * @param query - Search query (barcode or product name)
 * @returns Array of matching products
 */
export const searchProducts = async (query: string) => {
  const response = await api.get('/products/search/', {
    params: { q: query },
  })
  return response.data
}

export default api

