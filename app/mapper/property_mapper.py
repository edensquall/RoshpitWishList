from app.dtos.property_dto import PropertyDTO
from app.mapper.base_mapper import BaseMapper
from app.models.property import Property


class PropertyMapper(BaseMapper[PropertyDTO, Property]):

    def to_model(self, dto: PropertyDTO) -> Property:
        model = None
        if dto:
            model = Property(
                id=dto.id,
                name=dto.name,
                type=dto.type,
                min=dto.min,
                max=dto.max,
                item_id=dto.item_id,
                create_date=dto.create_date,
                modify_date=dto.modify_date
            )
        return model

    def to_dto(self, model: Property) -> PropertyDTO:
        dto = None
        if model:
            dto = PropertyDTO(
                id=model.id,
                name=model.name,
                type=model.type,
                min=model.min,
                max=model.max,
                item_id=model.item_id,
                create_date=model.create_date,
                modify_date=model.modify_date
            )
        return dto
