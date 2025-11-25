.PHONY: help install-backend install-frontend install dev-backend dev-frontend dev docker-up docker-down clean

help:
	@echo "Comandos disponibles:"
	@echo "  make install          - Instalar todas las dependencias"
	@echo "  make install-backend  - Instalar dependencias del backend"
	@echo "  make install-frontend - Instalar dependencias del frontend"
	@echo "  make dev              - Ejecutar backend y frontend en desarrollo"
	@echo "  make dev-backend      - Ejecutar solo backend"
	@echo "  make dev-frontend     - Ejecutar solo frontend"
	@echo "  make docker-up        - Levantar contenedores con Docker"
	@echo "  make docker-down      - Detener contenedores Docker"
	@echo "  make clean            - Limpiar archivos temporales"

install: install-backend install-frontend

install-backend:
	@echo "Instalando dependencias del backend..."
	cd backend && python -m venv venv
	cd backend && venv\Scripts\activate && pip install -r requirements.txt

install-frontend:
	@echo "Instalando dependencias del frontend..."
	cd frontend && npm install

dev-backend:
	@echo "Ejecutando backend..."
	cd backend && python manage.py runserver

dev-frontend:
	@echo "Ejecutando frontend..."
	cd frontend && npm run dev

docker-up:
	@echo "Levantando contenedores..."
	docker-compose up -d

docker-down:
	@echo "Deteniendo contenedores..."
	docker-compose down

clean:
	@echo "Limpiando archivos temporales..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".next" -exec rm -rf {} +
	find . -type d -name "node_modules" -exec rm -rf {} +

