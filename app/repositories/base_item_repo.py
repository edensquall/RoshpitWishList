from abc import abstractmethod
from typing import List

from app.models.item import Item
from app.models.property import Property
from app.repositories.base_repo import BaseRepo


class BaseItemRepo(BaseRepo[Item]):

    @abstractmethod
    def get_item_property(self, property: Property) -> List[Property]:
        raise NotImplementedError

    @abstractmethod
    def get_by_item_type(self, item: Item) -> List[Item]:
        raise NotImplementedError
