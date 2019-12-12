from typing import List

from injector import inject

from app.models.item import Item
from app.models.item_type import ItemType
from app.models.property import Property
from app.models.wish import Wish
from app.models.wish_property import WishProperty
from app.repositories.base_item_repo import BaseItemRepo
from app.repositories.base_item_type_repo import BaseItemTypeRepo
from app.repositories.base_property_repo import BasePropertyRepo
from app.repositories.base_wish_property_repo import BaseWishPropertyRepo
from app.repositories.base_wish_repo import BaseWishRepo
from app.services.base_wish_list_service import BaseWishListService
from app.unit_of_works.base_uow import BaseUOW


class WishListService(BaseWishListService):

    @inject
    def __init__(self, wish_repo: BaseWishRepo, wish_property_repo: BaseWishPropertyRepo, item_repo: BaseItemRepo,
                 item_type_repo: BaseItemTypeRepo, property_repo: BasePropertyRepo, uow: BaseUOW):
        self.wish_repo = wish_repo
        self.wish_property_repo = wish_property_repo
        self.item_type_repo = item_type_repo
        self.item_repo = item_repo
        self.property_repo = property_repo
        self.uow = uow

    def get_wish_by_id(self, wish: Wish) -> Wish:
        """
        取得符合此id的wish資料
        Args:
            wish: 傳遞wish參數

        Returns: 符合此id的wish資料

        """
        return self.wish_repo.get_by_id(wish)

    def add_new_wish(self, wish: Wish) -> None:
        """
        新增wish的資料
        Args:
            wish: 傳遞wish參數

        Returns: None

        """
        with self.uow.auto_complete():
            self.wish_repo.insert(wish)

    def get_user_wishes(self, wish: Wish) -> List[Wish]:
        """
        取得某個使用者的所有wish
        Args:
            wish: 傳遞wish參數

        Returns: 某個使用者的所有wish

        """
        return self.wish_repo.get_by_user_id(wish)

    def delete_wish_from_list(self, wish: Wish) -> None:
        """
        刪除wish的資料
        Args:
            wish: 傳遞wish參數

        Returns: None

        """
        with self.uow.auto_complete():
            self.wish_property_repo.delete_by_wish_id(WishProperty(wish_id=wish.id))
            self.wish_repo.delete(wish)

    def get_all_item_types(self) -> List[ItemType]:
        """
        取得所有道具資料
        Returns: 所有道具資料

        """
        return self.item_type_repo.get_all(ItemType)

    def get_all_these_types_of_items(self, item: Item) -> List[Item]:
        """
        取得所有該類型的道具
        Args:
            item: 傳遞道具參數

        Returns: 所有該類型的道具

        """
        return self.item_repo.get_by_item_type(item)

    def get_all_the_property_of_this_item(self, property: Property) -> List[Property]:
        """
        取得某個道具的屬性
        Args:
            property: 傳遞屬性參數

        Returns: 某個道具的屬性

        """
        return self.item_repo.get_item_property(property)
