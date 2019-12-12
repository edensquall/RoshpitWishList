from abc import abstractmethod
from typing import List

from app.models.notify import Notify
from app.repositories.base_repo import BaseRepo


class BaseNotifyRepo(BaseRepo[Notify]):

    @abstractmethod
    def get_by_user_id(self, notify: Notify) -> List[Notify]:
        """
        取得某個user的所有通知資料
        Args:
            notify: 傳遞通知參數

        Returns: 某個user的所有通知資料

        """
        raise NotImplementedError
