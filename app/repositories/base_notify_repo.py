from abc import abstractmethod
from typing import List

from app.models.notify import Notify
from app.repositories.base_repo import BaseRepo


class BaseNotifyRepo(BaseRepo[Notify]):

    @abstractmethod
    def get_by_user_id(self, notify: Notify) -> List[Notify]:
        raise NotImplementedError
