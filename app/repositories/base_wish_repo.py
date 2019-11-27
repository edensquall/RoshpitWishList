from abc import abstractmethod
from typing import List

from app.models.wish import Wish
from app.repositories.base_repo import BaseRepo


class BaseWishRepo(BaseRepo[Wish]):

    @abstractmethod
    def get_by_user_id(self, wish: Wish) -> List[Wish]:
        raise NotImplementedError
