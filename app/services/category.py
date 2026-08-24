from sqlalchemy.orm import Session
from app.repositories.category import CategoryRepository
from app.schemas.category import CategoryCreate, CategoryRead

class CatNotFound(Exception):
     """Category is not found in data base"""

class CatService:
    def __init__(self, db: Session) -> None:
            self.db = db
            self.cat_repository = CategoryRepository(db)

    def list_cats(self) -> list[CategoryRead]:
        cats = self.cat_repository.get_all()
        return [CategoryRead.model_validate(cat) for cat in cats]

    def create_cat(self, cat_create=CategoryCreate) -> CategoryRead:
        new_cat = self.cat_repository.create(name=cat_create.name)
        self.db.commit()
        return CategoryRead.model_validate(new_cat)

    def update_cat(self, cat_id: str, cat_update: CategoryCreate) -> CategoryRead:
        cat_for_update = self.cat_repository.get_by_id(cat_id=cat_id)
        if not cat_for_update:
            raise CatNotFound(f'Category {cat_id} is not found')

        if cat_update.name is not None:
            cat_for_update.name = cat_update.name
        self.db.commit()
        return CategoryRead.model_validate(cat_update)

    def delete_cat(self, cat_id: str) -> None:
        cat_for_delete = self.cat_repository.get_by_id(cat_id=cat_id)
        if not cat_for_delete:
            raise CatNotFound(f'Category {cat_id} is not found')

        self.cat_repository.delete(cat_for_delete)
        self.db.commit()