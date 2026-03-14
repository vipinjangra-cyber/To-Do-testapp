from fastapi import FastAPI, Depends, Body
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import model
from database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Todo API running"}

@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(model.Task).all()

@app.post("/tasks")
def create_task(title: str = Body(...), db: Session = Depends(get_db)):
    task = model.Task(title=title, completed=False)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(model.Task).filter(model.Task.id == task_id).first()
    db.delete(task)
    db.commit()
    return {"message": "Task deleted"}

@app.put("/tasks/{task_id}")
def complete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(model.Task).filter(model.Task.id == task_id).first()
    task.completed = True
    db.commit()
    db.refresh(task)
    return {"message": "Task completed"}