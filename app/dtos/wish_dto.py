from dataclasses import dataclass, field
from datetime import date
from typing import List

from app.dtos.item_dto import ItemDTO
from app.dtos.wish_property_dto import WishPropertyDTO


@dataclass
class WishDTO:
    id: int = None
    currency: int = None
    min_level: int = None
    max_bid: int = None
    max_buyout: int = None
    user_id: int = None
    item_id: int = None
    item_type: int = None
    create_date: date = None
    modify_date: date = None
    item: ItemDTO = None
    wish_properties: List[WishPropertyDTO] = field(default_factory=list)
