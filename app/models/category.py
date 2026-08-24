from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class CatORM(Base):
    __tablename__ = "categories"

    name: Mapped[str]