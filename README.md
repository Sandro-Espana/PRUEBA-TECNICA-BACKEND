# Backend - Sistema de Control de Marcas

## Instalación
1. Crear entorno virtual: `python -m venv .venv`
2. Activar entorno: `.venv\Scripts\activate` (Windows) o `source .venv/bin/activate` (Linux/Mac)
3. Instalar dependencias: `pip install -r requirements.txt`
4. Ejecutar: `uvicorn app.main:app --reload`

## Endpoints disponibles
- GET/POST /api/v1/trademark
- GET/PUT/DELETE /api/v1/trademark/{id}
- GET/POST /brands (compatibilidad)
