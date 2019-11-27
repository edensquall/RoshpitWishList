from app.dtos.item_type_dto import ItemTypeDTO
from app.mapper.base_mapper import BaseMapper
from app.models.item_type import ItemType


class ItemTypeMapper(BaseMapper[ItemTypeDTO, ItemType]):

    def to_model(self, dto: ItemTypeDTO) -> ItemType:
        model = None
        if dto:
            model = ItemType(
                id=dto.id,
                code=dto.code,
                name=dto.name,
                create_date=dto.create_date,
                modify_date=dto.modify_date
            )
        return model

    def to_dto(self, model: ItemType) -> ItemTypeDTO:
        dto = None
        if model:
            dto = ItemTypeDTO(
                id=model.id,
                code=model.code,
                name=model.name,
                create_date=model.create_date,
                modify_date=model.modify_date
            )
        return dto
