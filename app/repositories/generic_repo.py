from typing import List, Type

from app.models import db
from app.repositories.base_repo import BaseRepo, T


class GenericRepo(BaseRepo[T]):

    def get_all(self, model_class: Type[T]) -> List[T]:
        return db.session.query(model_class).all()

    def get_by_id(self, model: T) -> T:
        return model.query.filter_by(id=model.id).first()

    def insert(self, model: T) -> None:
        db.session.merge(model)
        db.session.flush()

    def delete_all(self, model_class: Type[T]) -> None:
        db.execute('SET FOREIGN_KEY_CHECKS = 0')
        db.session.query(model_class).delete()
        db.execute('SET FOREIGN_KEY_CHECKS = 1')

    def delete(self, model: T) -> None:
        model.query.filter_by(id=model.id).delete()
