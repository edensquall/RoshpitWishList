from abc import abstractmethod

from app.models.property import Property
from app.repositories.base_repo import BaseRepo


class BasePropertyRepo(BaseRepo[Property]):

    @abstractmethod
    def get_property_type_count(self) -> int:
        raise NotImplementedError
