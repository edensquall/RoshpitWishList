from typing import List, Type

from app.models import db
from app.repositories.base_repo import BaseRepo, T


class GenericRepo(BaseRepo[T]):

    def get_all(self, model_class: Type[T]) -> List[T]:
        """
        取得某類別的所有資料
        Args:
            model_class: 某類別本身

        Returns: 某類別的所有資料

        """
        return db.session.query(model_class).all()

    def get_by_id(self, model: T) -> T:
        """
        取得某類別符合此id的資料
        Args:
            model: 傳遞某類別參數

        Returns: 某類別符合此id的資料

        """
        return model.query.filter_by(id=model.id).first()

    def insert(self, model: T) -> None:
        """
        新增某類別的資料
        Args:
            model: 傳遞某類別參數

        Returns: None

        """
        db.session.merge(model)
        db.session.flush()

    def delete_all(self, model_class: Type[T]) -> None:
        """
        刪除某類別的所有資料
        Args:
            model_class: 某類別本身

        Returns: None

        """
        db.execute('SET FOREIGN_KEY_CHECKS = 0')
        db.session.query(model_class).delete()
        db.execute('SET FOREIGN_KEY_CHECKS = 1')

    def delete(self, model: T) -> None:
        """
        刪除某類別的資料
        Args:
            model: 傳遞某類別參數

        Returns: None

        """
        model.query.filter_by(id=model.id).delete()
