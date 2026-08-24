from pydantic import BaseModel, ConfigDict


class TaskRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    title: str
    completed: bool

class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: str | None = None # none = none это возможный вариант если мы не получили одну из строк, то есть если мы получили только completed, то title становиться none
    completed: bool | None = None