from app.dtos.item_dto import ItemDTO
from app.mapper.base_mapper import BaseMapper
from app.mapper.property_mapper import PropertyMapper
from app.models.item import Item


class ItemMapper(BaseMapper[ItemDTO, Item]):

    def __init__(self):
        self.view_property_mapper = PropertyMapper()

    def to_model(self, dto: ItemDTO) -> Item:
        model = None
        if dto:
            model = Item(
                id=dto.id,
                code=dto.code,
                name=dto.name,
                img=dto.img,
                type=dto.type,
                rarity=dto.rarity,
                create_date=dto.create_date,
                modify_date=dto.modify_date,
                properties=[self.view_property_mapper.to_model(property) for property in dto.properties]
            )
        return model

    def to_dto(self, model: Item) -> ItemDTO:
        dto = None
        if model:
            dto = ItemDTO(
                id=model.id,
                code=model.code,
                name=model.name,
                img=model.img,
                type=model.type,
                rarity=model.rarity,
                create_date=model.create_date,
                modify_date=model.modify_date,
                properties=[self.view_property_mapper.to_dto(property) for property in model.properties]
            )
        return dto
