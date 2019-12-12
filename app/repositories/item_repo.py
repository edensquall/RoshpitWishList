from typing import List

from app.models.item import Item
from app.models.property import Property
from app.repositories.base_item_repo import BaseItemRepo
from app.repositories.generic_repo import GenericRepo


class ItemRepo(GenericRepo[Item], BaseItemRepo):

    def get_item_property(self, property: Property) -> List[Property]:
        """
        取得某個道具的屬性
        Args:
            property: 傳遞屬性參數

        Returns: 某個道具的屬性

        """
        return Property.query.order_by(Property.type).filter_by(item_id=property.item_id).all()

    def get_by_item_type(self, item: Item) -> List[Item]:
        """
        取得某個類型的道具
        Args:
            item: 傳遞道具參數

        Returns: 某個類型的道具

        """
        if item.type == 0:
            return Item.query.all()
        return Item.query.filter_by(type=item.type).all()
