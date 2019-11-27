from app.models.item_type import ItemType
from app.repositories.base_item_type_repo import BaseItemTypeRepo
from app.repositories.generic_repo import GenericRepo


class ItemTypeRepo(GenericRepo[ItemType], BaseItemTypeRepo):
    pass
