/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  env: {
    API_URL: process.env.API_URL || 'http://localhost:8000/api',
  },
  // Para Docker standalone build (solo en producción)
  ...(process.env.NODE_ENV === 'production' && { output: 'standalone' }),
  // Configuración para hot reload en Docker
  webpackDevMiddleware: config => {
    config.watchOptions = {
      poll: 1000, // Check for changes every second
      aggregateTimeout: 300,
    }
    return config
  },
}

module.exports = nextConfig

