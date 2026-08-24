from app.api.dependencies import get_task_service
from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.task import TaskCreate, TaskUpdate, TaskRead
from app.services.task import TaskNotFound, TaskService

router = APIRouter("/tasks")

@router.get("")
def read_tasks(task_service: TaskService = Depends(get_task_service)):
    return task_service.list_tasks()

@router.post("", status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate, task_service: TaskService = Depends(get_task_service)) -> TaskRead:
    try:
        return task_service.create_task(task_create=payload)
    except TaskNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.patch("/{task_id}")
def reload_task(task_id: str, payload: TaskUpdate, task_service: TaskService = Depends(get_task_service)) -> TaskRead:
    return task_service.update_task(task_id=task_id, task_update=payload)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: str, task_service: TaskService = Depends(get_task_service)):
    try:
        return task_service.delete_task(task_id=task_id)
    except TaskNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
