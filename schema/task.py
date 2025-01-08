from pydantic import BaseModel

class Task(BaseModel):
    id: int
    name: str
    description: str
    pomodoro_count: int
    category_id: int
