from pydantic import BaseModel, Field


class TaskAddSchema(BaseModel):
    name: str
    description: str | None

    class Config:
        orm_mode = True


class TaskSchema(TaskAddSchema):
    id: int

    class Config:
        orm_mode = True


class TaskIdSchema(BaseModel):
    success: bool = True
    task_id: int
