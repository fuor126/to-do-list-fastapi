from contextlib import asynccontextmanager
from uuid import uuid4
from fastapi import Depends, FastAPI, status
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.orm import Mapped, Session

from app.models import Base
from app.db.session import engine
from app.api.routers.task import router as task_router
# uvicorn main:app --port 8080 --reload
# docker run --name pg-container -e POSTGRES_PASSWORD=admin -d -p 15432:5432 postgres - создать pg-container
# docker exec -it pg-container psql -U postgres -d postgres - консоль управления постгрес

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router=task_router)

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)