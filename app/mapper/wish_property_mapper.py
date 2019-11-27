from app.dtos.wish_property_dto import WishPropertyDTO
from app.mapper.base_mapper import BaseMapper
from app.mapper.property_mapper import PropertyMapper
from app.models.wish_property import WishProperty


class WishPropertyMapper(BaseMapper[WishPropertyDTO, WishProperty]):

    def __init__(self):
        self.property_mapper = PropertyMapper()

    def to_model(self, dto: WishPropertyDTO) -> WishProperty:
        model = None
        if dto:
            model = WishProperty(
                id=dto.id,
                roll=dto.roll,
                property_id=dto.property_id,
                wish_id=dto.wish_id,
                create_date=dto.create_date,
                modify_date=dto.modify_date,
                property=self.property_mapper.to_model(dto.property),
            )
        return model

    def to_dto(self, model: WishProperty) -> WishPropertyDTO:
        dto = None
        if model:
            dto = WishPropertyDTO(
                id=model.id,
                roll=model.roll,
                property_id=model.property_id,
                wish_id=model.wish_id,
                create_date=model.create_date,
                modify_date=model.modify_date,
                property=self.property_mapper.to_dto(model.property)
            )
        return dto
