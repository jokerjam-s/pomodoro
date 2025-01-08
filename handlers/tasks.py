from typing import List

from fastapi import APIRouter

from fixtures import tasks
from schema.task import Task

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/all", response_model=List[Task])
async def index():
    return tasks


@router.post("/", response_model=Task)
async def create_task(task: Task):
    tasks.append(task)
    return task


@router.get("/{task_id}", response_model=Task)
async def get_task_by_id(task_id):
    for task in tasks:
        if task.id == task_id:
            return task


@router.put("/{task_id}")
async def update_task(task_id: int, task: Task):
    return {"message": "Hello World"}


@router.delete("/{task_id}")
async def delete_task(task_id):
    return {"message": "Hello World"}


@router.patch("/{task_id}")
async def update_task(task_id, task):
    return {"message": "Hello World"}
