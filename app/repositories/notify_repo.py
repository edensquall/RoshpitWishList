from typing import List

from app.models.notify import Notify
from app.repositories.base_notify_repo import BaseNotifyRepo
from app.repositories.generic_repo import GenericRepo


class NotifyRepo(GenericRepo[Notify], BaseNotifyRepo):

    def get_by_user_id(self, notify: Notify) -> List[Notify]:
        """
        取得某個user的所有通知資料
        Args:
            notify: 傳遞通知參數

        Returns: 某個user的所有通知資料

        """
        return Notify.query.filter_by(user_id=Notify.user_id).all()
