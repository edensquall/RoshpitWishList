from app.models.property import Property
from app.repositories.base_property_repo import BasePropertyRepo
from app.repositories.generic_repo import GenericRepo


class PropertyRepo(GenericRepo[Property], BasePropertyRepo):
    pass
