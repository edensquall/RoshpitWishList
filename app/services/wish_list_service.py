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


class ViewPropertyMapper(object):
    pass


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
        return self.wish_repo.get_by_id(wish)

    def add_new_wish(self, wish: Wish) -> None:
        with self.uow.auto_complete():
            self.wish_repo.insert(wish)

    def get_user_wishes(self, wish: Wish) -> List[Wish]:
        return self.wish_repo.get_by_user_id(wish)

    def delete_wish_from_list(self, wish: Wish) -> None:
        with self.uow.auto_complete():
            self.wish_property_repo.delete_by_wish_id(WishProperty(wish_id=wish.id))
            self.wish_repo.delete(wish)

    def get_all_item_types(self) -> List[ItemType]:
        return self.item_type_repo.get_all(ItemType)

    def get_all_these_types_of_items(self, item: Item) -> List[Item]:
        return self.item_repo.get_by_item_type(item)

    def get_property_type_count_of_this_item(self) -> int:
        return self.property_repo.get_property_type_count()

    def get_all_the_property_of_this_item(self, property: Property) -> List[Property]:
        return self.item_repo.get_item_property(property)
