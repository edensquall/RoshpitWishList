from abc import abstractmethod

from app.models.wish_property import WishProperty
from app.repositories.base_repo import BaseRepo


class BaseWishPropertyRepo(BaseRepo[WishProperty]):

    @abstractmethod
    def get_by_wish_id(self, wish_property: WishProperty) -> WishProperty:
        raise NotImplementedError

    @abstractmethod
    def delete_by_wish_id(self, wish_property: WishProperty) -> None:
        raise NotImplementedError
