# API de Gestión de Tareas

*Autor:* Miguel Angel Quintero Aragón  
*Código:* 408592  
https://youtube.com/shorts/qvOpl8tD55Y?si=t_pyDMXOKIg1nZyf
##  Descripción
API REST creada con *FastAPI* para gestionar tareas con los estados:
todo, doing, done.

## Endpoints principales
- GET /tasks
- GET /tasks/:id
- POST /tasks
- PUT /tasks/:id
- PATCH /tasks/:id/status
- DELETE /tasks/:id
- GET /tasks/summary

##  Ejecución
```bash
uvicorn app.main:app --reload
Gestor de Tareas FullStack
==========================

Contenido:
  - backend/: FastAPI app (Python)
  - frontend/: Vue 3 + Vite + Tailwind frontend

Requisitos:
  - Python 3.8+ y pip
  - Node.js y npm

Backend (ejecutar):
  cd backend
  pip install -r requirements.txt
  uvicorn main:app --reload --port 8000

Frontend (ejecutar):
  cd frontend
  npm install
  npm run dev

Notas:
  - El backend corre en http://127.0.0.1:8000
  - El frontend por defecto corre en http://localhost:5173
  - CORS ya está habilitado en el backend para permitir peticiones desde el frontend
