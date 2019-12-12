from abc import abstractmethod
from typing import List

from injector import inject

from app.models.item import Item
from app.models.item_type import ItemType
from app.models.property import Property
from app.models.wish import Wish
from app.repositories.base_item_repo import BaseItemRepo
from app.repositories.base_item_type_repo import BaseItemTypeRepo
from app.repositories.base_property_repo import BasePropertyRepo
from app.repositories.base_wish_property_repo import BaseWishPropertyRepo
from app.repositories.base_wish_repo import BaseWishRepo
from app.unit_of_works.base_uow import BaseUOW


class BaseWishListService:

    @inject
    def __init__(self, wish_repo: BaseWishRepo, wish_property_repo: BaseWishPropertyRepo, item_repo: BaseItemRepo,
                 item_type_repo: BaseItemTypeRepo, property_repo: BasePropertyRepo, uow: BaseUOW):
        raise NotImplementedError

    @abstractmethod
    def get_wish_by_id(self, wish: Wish) -> Wish:
        """
        取得符合此id的wish資料
        Args:
            wish: 傳遞wish參數

        Returns: 符合此id的wish資料

        """
        raise NotImplementedError

    @abstractmethod
    def add_new_wish(self, wish: Wish) -> None:
        """
        新增wish的資料
        Args:
            wish: 傳遞wish參數

        Returns: None

        """
        raise NotImplementedError

    @abstractmethod
    def get_user_wishes(self, wish: Wish) -> List[Wish]:
        """
        取得某個使用者的所有wish
        Args:
            wish: 傳遞wish參數

        Returns: 某個使用者的所有wish

        """
        raise NotImplementedError

    @abstractmethod
    def delete_wish_from_list(self, wish_: Wish) -> None:
        """
        刪除wish的資料
        Args:
            wish: 傳遞wish參數

        Returns: None

        """
        raise NotImplementedError

    @abstractmethod
    def get_all_item_types(self) -> List[ItemType]:
        """
        取得所有道具資料
        Returns: 所有道具資料

        """
        raise NotImplementedError

    @abstractmethod
    def get_all_these_types_of_items(self, item: Item) -> List[Item]:
        """
        取得所有該類型的道具
        Args:
            item: 傳遞道具參數

        Returns: 所有該類型的道具

        """
        raise NotImplementedError

    @abstractmethod
    def get_all_the_property_of_this_item(self, property: Property) -> List[Property]:
        """
        取得某個道具的屬性
        Args:
            property: 傳遞屬性參數

        Returns: 某個道具的屬性

        """
        raise NotImplementedError
