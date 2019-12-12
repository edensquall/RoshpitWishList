from abc import abstractmethod
from typing import List

from app.models.wish import Wish
from app.repositories.base_repo import BaseRepo


class BaseWishRepo(BaseRepo[Wish]):

    @abstractmethod
    def get_by_user_id(self, wish: Wish) -> List[Wish]:
        """
        取得某個使用者的所有wish
        Args:
            wish: 傳遞Wish參數

        Returns: 某個使用者的所有wish

        """
        raise NotImplementedError
