from sqlalchemy import func

from app.models import *
from app.models.property import Property
from app.repositories.base_property_repo import BasePropertyRepo
from app.repositories.generic_repo import GenericRepo


class PropertyRepo(GenericRepo[Property], BasePropertyRepo):

    def get_property_type_count(self) -> int:
        return db.session.query(func.max(Property.type)).scalar()
