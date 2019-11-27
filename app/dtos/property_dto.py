from dataclasses import dataclass
from datetime import date


@dataclass
class PropertyDTO:
    id: int = None
    name: str = None
    type: int = None
    min: int = None
    max: int = None
    item_id: int = None
    create_date: date = None
    modify_date: date = None
