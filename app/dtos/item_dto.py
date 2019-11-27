from dataclasses import dataclass, field
from datetime import date
from typing import List

from app.dtos.property_dto import PropertyDTO


@dataclass
class ItemDTO:
    id: int = None
    code: str = None
    name: str = None
    img: str = None
    type: int = None
    rarity: str = None
    create_date: date = None
    modify_date: date = None
    properties: List[PropertyDTO] = field(default_factory=list)
