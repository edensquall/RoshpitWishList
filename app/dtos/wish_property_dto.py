from dataclasses import dataclass
from datetime import date

from app.dtos.property_dto import PropertyDTO


@dataclass
class WishPropertyDTO:
    id: int = None
    roll: int = None
    property_id: int = None
    wish_id: int = None
    create_date: date = None
    modify_date: date = None
    property: PropertyDTO = None
