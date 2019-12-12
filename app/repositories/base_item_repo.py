from abc import abstractmethod
from typing import List

from app.models.item import Item
from app.models.property import Property
from app.repositories.base_repo import BaseRepo


class BaseItemRepo(BaseRepo[Item]):

    @abstractmethod
    def get_item_property(self, property: Property) -> List[Property]:
        """
        取得某個道具的屬性
        Args:
            property: 傳遞屬性參數

        Returns: 某個道具的屬性

        """
        raise NotImplementedError

    @abstractmethod
    def get_by_item_type(self, item: Item) -> List[Item]:
        """
        取得某個類型的道具
        Args:
            item: 傳遞道具參數

        Returns: 某個類型的道具

        """
        raise NotImplementedError
