from typing import List

from fastapi import APIRouter

from database import get_db_connection
from fixtures import tasks
from schema.task import Task

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/all", response_model=List[Task])
async def index():
    result: List[Task] = []
    cursor = get_db_connection().cursor()
    tasks = cursor.execute("SELECT * FROM tasks").fetchall()
    for task in tasks:
        result.append(Task(id=task[0], name=task[1], description=task[2], pomodoro_count=task[3], category_id=task[4]))
    return result


@router.post("/", response_model=Task)
async def create_task(task: Task):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Tasks (id, name, description, pomodoro_count, category_id) VALUES (?, ?, ?, ?, ?)",
                   (task.id, task.name, task.description, task.pomodoro_count, task.category_id))

    connection.commit()
    connection.close()
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
