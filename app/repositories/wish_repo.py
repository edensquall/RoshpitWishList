from typing import List, TypeVar

from app.models.wish import Wish
from app.repositories.base_wish_repo import BaseWishRepo
from app.repositories.generic_repo import GenericRepo

T = TypeVar('T')


class WishRepo(GenericRepo[Wish], BaseWishRepo):

    def get_by_user_id(self, wish: Wish) -> List[Wish]:
        return Wish.query.filter_by(user_id=wish.user_id).order_by(Wish.create_date.desc()).all()
