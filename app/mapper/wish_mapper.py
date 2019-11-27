from app.dtos.wish_dto import WishDTO
from app.mapper.base_mapper import BaseMapper
from app.mapper.item_mapper import ItemMapper
from app.mapper.wish_property_mapper import WishPropertyMapper
from app.models.wish import Wish


class WishMapper(BaseMapper[WishDTO, Wish]):

    def __init__(self):
        self.item_mapper = ItemMapper()
        self.wish_property_mapper = WishPropertyMapper()

    def to_model(self, dto: Wish) -> Wish:
        model = None
        if dto:
            model = Wish(
                id=dto.id,
                currency=dto.currency,
                min_level=dto.min_level,
                max_bid=dto.max_bid,
                max_buyout=dto.max_buyout,
                user_id=dto.user_id,
                item_id=dto.item_id,
                create_date=dto.create_date,
                modify_date=dto.modify_date,
                item=self.item_mapper.to_model(dto.item),
                wish_properties=[self.wish_property_mapper.to_model(wish_property) for wish_property in
                                 dto.wish_properties]
            )
        return model

    def to_dto(self, model: Wish) -> WishDTO:
        dto = None
        if model:
            dto = WishDTO(
                id=model.id,
                currency=model.currency,
                min_level=model.min_level,
                max_bid=model.max_bid,
                max_buyout=model.max_buyout,
                user_id=model.user_id,
                item_id=model.item_id,
                item_type=model.item.type,
                create_date=model.create_date,
                modify_date=model.modify_date,
                item=self.item_mapper.to_dto(model.item),
                wish_properties=[self.wish_property_mapper.to_dto(wish_property) for wish_property in
                                 model.wish_properties]
            )
        return dto
