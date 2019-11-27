from typing import List

from app.models.notify import Notify
from app.repositories.base_notify_repo import BaseNotifyRepo
from app.repositories.generic_repo import GenericRepo


class NotifyRepo(GenericRepo[Notify], BaseNotifyRepo):

    def get_by_user_id(self, notify: Notify) -> List[Notify]:
        return Notify.query.filter_by(user_id=Notify.user_id).all()
