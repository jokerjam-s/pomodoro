from pydantic import BaseModel, field_validator, model_validator


class Task(BaseModel):
    id: int
    name: str | None = None
    description: str
    pomodoro_count: int | None = None
    category_id: int

    @model_validator(mode="after")
    def check_name_or_pomodoro_count_is_not_none(self):
        print(self)
        return self

