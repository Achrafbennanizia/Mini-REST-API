from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, Session
from typing import List
from ..models import Task, TaskRead, TaskCreate, TaskUpdate
from ..database import get_session

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("", response_model=TaskRead, status_code=201)
def create_task(payload: TaskCreate, session: Session = Depends(get_session)):
task = Task(**payload.dict())
session.add(task)
session.commit()
session.refresh(task)
return task

@router.get("", response_model=List[TaskRead])
def list_tasks(session: Session = Depends(get_session)):
results = session.exec(select(Task).order_by(Task.created_at.desc())).all()
return results

@router.get("/{task_id}", response_model=TaskRead)
def get_task(task_id: int, session: Session = Depends(get_session)):
task = session.get(Task, task_id)
if not task:
raise HTTPException(404, "Task not found")
return task

@router.put("/{task_id}", response_model=TaskRead)
def update_task(task_id: int, payload: TaskUpdate, session: Session = Depends(get_session)):
task = session.get(Task, task_id)
if not task:
raise HTTPException(404, "Task not found")
data = payload.dict(exclude_unset=True)
for k, v in data.items():
setattr(task, k, v)
session.add(task)
session.commit()
session.refresh(task)
return task

@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int, session: Session = Depends(get_session)):
task = session.get(Task, task_id)
if not task:
raise HTTPException(404, "Task not found")
session.delete(task)
session.commit()
return None