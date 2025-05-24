from fastapi import APIRouter, HTTPException, Depends
from typing import List
from ...models.task import Task
from ...auth.sucurity import get_current_user
from src.database.db import tasks_db

router = APIRouter()


@router.post("/", response_model=Task)
async def create_task(task: Task, current_user=Depends(get_current_user)):
    if any(t.id == task.id for t in tasks_db):
        raise HTTPException(status_code=400, detail="Task ID already exists")
    tasks_db.append(task)
    return task


@router.get("/", response_model=List[Task])
async def get_tasks(current_user=Depends(get_current_user)):
    return tasks_db


@router.get("/{task_id}", response_model=Task)
async def get_task(task_id: int, current_user=Depends(get_current_user)):
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@router.put("/{task_id}", response_model=Task)
async def update_task(task_id: int, updated_task: Task, current_user=Depends(get_current_user)):
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")


@router.delete("/{task_id}")
async def delete_task(task_id: int, current_user=Depends(get_current_user)):
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db.pop(index)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
