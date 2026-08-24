from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.category import CatORM

class CategoryRepository:
    def __init__(self, db: Session) -> None:
            self.db = db

    def get_all(self) -> list[CatORM]:
        return self.db.scalars(select(CatORM)).all()

    def get_by_id(self, cat_id: str) -> CatORM:
        return self.db.get(CatORM, cat_id)

    def create(self, cat_name: str) -> CatORM:
        new_cat = CatORM(name=cat_name)
        self.db.add(new_cat)
        return new_cat

    def delete(self, CatORM) -> None:
        self.db.delete(CatORM)