from abc import abstractmethod

from app.models.wish_property import WishProperty
from app.repositories.base_repo import BaseRepo


class BaseWishPropertyRepo(BaseRepo[WishProperty]):

    @abstractmethod
    def get_by_wish_id(self, wish_property: WishProperty) -> WishProperty:
        """
        取得某個wish的所有wish property
        Args:
            wish_property: 傳遞WishProperty參數

        Returns: 某個wish的所有wish property

        """
        raise NotImplementedError

    @abstractmethod
    def delete_by_wish_id(self, wish_property: WishProperty) -> None:
        """
        刪除某個wish的所有wish property
        Args:
            wish_property: 傳遞WishProperty參數

        Returns: None

        """
        raise NotImplementedError
