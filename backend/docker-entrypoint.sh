#!/bin/bash

# Script de inicialización para el contenedor Django

echo "Esperando a que la base de datos esté lista..."
sleep 3

echo "Aplicando migraciones..."
python manage.py migrate --noinput

echo "Recolectando archivos estáticos..."
python manage.py collectstatic --noinput --clear

echo "Iniciando servidor Django..."
exec "$@"

