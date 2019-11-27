from sqlalchemy.util.compat import contextmanager

from app.models import db
from app.unit_of_works.base_uow import BaseUOW


class SQLAlchemyUOW(BaseUOW):

    def complete(self):
        db.session.commit()

    def rollback(self):
        db.session.rollback()

    @contextmanager
    def auto_complete(self):
        try:
            yield
            self.complete()
        except Exception as e:
            self.rollback()
            raise e
