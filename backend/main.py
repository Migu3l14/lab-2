from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI(title="API - Gestor de Tareas")

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = Field("todo", regex="^(todo|doing|done)$")

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = Field(None, regex="^(todo|doing|done)$")

class Task(TaskBase):
    id: int

tasks_db: List[Task] = []
_next_id = 1

def _get_next_id():
    global _next_id
    nid = _next_id
    _next_id += 1
    return nid

@app.get("/")
def root():
    return {"message": "API de Tareas funcionando"}

@app.get("/task", response_model=List[Task])
def list_tasks():
    return tasks_db

@app.post("/task", response_model=Task, status_code=201)
def create_task(task: TaskCreate):
    new_task = Task(id=_get_next_id(), **task.dict())
    tasks_db.append(new_task)
    return new_task

@app.get("/task/{task_id}", response_model=Task)
def get_task(task_id: int):
    for t in tasks_db:
        if t.id == task_id:
            return t
    raise HTTPException(404, "Tarea no encontrada")

@app.put("/task/{task_id}", response_model=Task)
def replace_task(task_id: int, task: TaskCreate):
    for i, t in enumerate(tasks_db):
        if t.id == task_id:
            updated = Task(id=task_id, **task.dict())
            tasks_db[i] = updated
            return updated
    raise HTTPException(404, "Tarea no encontrada")

@app.patch("/task/{task_id}", response_model=Task)
def modify_task(task_id: int, task: TaskUpdate):
    for i, t in enumerate(tasks_db):
        if t.id == task_id:
            updated_data = t.dict()
            incoming = task.dict(exclude_unset=True)
            updated_data.update(incoming)
            updated = Task(**updated_data)
            tasks_db[i] = updated
            return updated
    raise HTTPException(404, "Tarea no encontrada")

@app.delete("/task/{task_id}", status_code=204)
def delete_task(task_id: int):
    for t in tasks_db:
        if t.id == task_id:
            tasks_db.remove(t)
            return
    raise HTTPException(404, "Tarea no encontrada")
