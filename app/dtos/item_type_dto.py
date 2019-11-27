from dataclasses import dataclass
from datetime import date


@dataclass
class ItemTypeDTO:
    id: int = None
    code: str = None
    name: str = None
    create_date: date = None
    modify_date: date = None
