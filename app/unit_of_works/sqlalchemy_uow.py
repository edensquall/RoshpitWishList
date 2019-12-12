from sqlalchemy.util.compat import contextmanager

from app.models import db
from app.unit_of_works.base_uow import BaseUOW


class SQLAlchemyUOW(BaseUOW):

    def complete(self):
        """
        完成後正式修改資料
        Returns: None

        """
        db.session.commit()

    def rollback(self):
        """
        回復資料
        Returns: None

        """
        db.session.rollback()

    @contextmanager
    def auto_complete(self):
        """
        自動完成資料的修改
        無錯誤 -> 正式修改資料
        有錯誤 -> 回復資料
        Returns: None

        """
        try:
            yield
            self.complete()
        except Exception as e:
            self.rollback()
            raise e
