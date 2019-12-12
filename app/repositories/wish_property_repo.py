from app.models.property import Property
from app.models.wish_property import WishProperty
from app.repositories.base_wish_property_repo import BaseWishPropertyRepo
from app.repositories.generic_repo import GenericRepo


class WishPropertyRepo(GenericRepo[WishProperty], BaseWishPropertyRepo):

    def get_by_wish_id(self, wish_property: WishProperty) -> WishProperty:
        """
        取得某個wish的所有wish property
        Args:
            wish_property: 傳遞WishProperty參數

        Returns: 某個wish的所有wish property

        """
        return WishProperty.query.filter_by(wish_id=wish_property.wish_id) \
            .join(Property, WishProperty.property) \
            .order_by(Property.name).all()

    def delete_by_wish_id(self, wish_property: WishProperty) -> None:
        """
        刪除某個wish的所有wish property
        Args:
            wish_property: 傳遞WishProperty參數

        Returns: None

        """
        WishProperty.query.filter_by(wish_id=wish_property.wish_id).delete()
