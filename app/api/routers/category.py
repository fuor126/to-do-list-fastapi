from app.api.dependencies import get_task_service
from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.category import TaskCreate, TaskUpdate, TaskRead
from app.services.task import TaskNotFound, TaskService