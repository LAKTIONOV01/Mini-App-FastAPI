from typing import Annotated

from fastapi import APIRouter, Depends

from schemas import TaskAddSchema, TaskSchema, TaskIdSchema
from repository import TaskRepository

router = APIRouter(
    prefix='/tasks',
    tags=['Tasks']
)


@router.post('')
async def add_task(task: Annotated[TaskAddSchema, Depends()]) -> TaskIdSchema:
    task_id = await TaskRepository.add_one(task)
    return {'ok': True, 'task_id': task_id}


@router.get('')
async def get_tasks():
    tasks = await TaskRepository.find_all()
    return {'tasks': tasks}
