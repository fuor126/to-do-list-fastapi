from sqlalchemy.orm import Session
from app.repositories.task import TaskRepository
from app.schemas.task import TaskRead, TaskCreate, TaskUpdate

class TaskNotFound(Exception):
    """Task is not found in db"""

class TaskService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.task_repository = TaskRepository(db)

    def list_tasks(self) -> list[TaskRead]:
        tasks = self.task_repository.get_all()
        return [TaskRead.model_validate(task) for task in tasks]

    def create_task(self, task_create: TaskCreate) -> TaskRead:
        task_created = self.task_repository.create(title=task_create.title)
        self.db.commit()
        return TaskRead.model_validate(task_created)

    def update_task(self, task_id: str, task_update: TaskUpdate) -> TaskRead:
        task_for_update = self.task_repository.get_by_id(task_id=task_id)
        if not task_for_update:
            raise TaskNotFound(f"Task {task_id} is not found")
        
        if task_update.title is not None:
            task_for_update.title = task_update.title
        elif task_update.completed is not None:
            task_for_update.completed = task_update.completed
        self.db.commit()
        return TaskRead.model_validate(task_update)
    
    def delete_task(self, task_id: str) -> TaskRead:
        task_for_delete = self.task_repository.get_by_id(task_id=task_id)
        if not task_for_delete:
            raise TaskNotFound(f"Task {task_id} is not found")  
         
        self.task_repository.delete(task_for_delete)
        self.db.commit()