from injector import Module

from app.repositories.base_item_repo import BaseItemRepo
from app.repositories.base_item_type_repo import BaseItemTypeRepo
from app.repositories.base_notify_repo import BaseNotifyRepo
from app.repositories.base_property_repo import BasePropertyRepo
from app.repositories.base_user_repo import BaseUserRepo
from app.repositories.base_wish_property_repo import BaseWishPropertyRepo
from app.repositories.base_wish_repo import BaseWishRepo
from app.repositories.item_repo import ItemRepo
from app.repositories.item_type_repo import ItemTypeRepo
from app.repositories.notify_repo import NotifyRepo
from app.repositories.property_repo import PropertyRepo
from app.repositories.user_repo import UserRepo
from app.repositories.wish_property_repo import WishPropertyRepo
from app.repositories.wish_repo import WishRepo
from app.services.auth_service import AuthService
from app.services.base_auth_service import BaseAuthService
from app.services.base_notification_service import BaseNotificationService
from app.services.base_wish_list_service import BaseWishListService
from app.services.notification_service import NotificationService
from app.services.wish_list_service import WishListService
from app.unit_of_works.base_uow import BaseUOW
from app.unit_of_works.sqlalchemy_uow import SQLAlchemyUOW


class AppModule(Module):
    def configure(self, binder):
        binder.bind(BaseUOW, to=SQLAlchemyUOW)

        binder.bind(BaseUserRepo, to=UserRepo)
        binder.bind(BaseWishRepo, to=WishRepo)
        binder.bind(BaseWishPropertyRepo, to=WishPropertyRepo)
        binder.bind(BaseItemTypeRepo, to=ItemTypeRepo)
        binder.bind(BaseItemRepo, to=ItemRepo)
        binder.bind(BasePropertyRepo, to=PropertyRepo)
        binder.bind(BaseNotifyRepo, to=NotifyRepo)

        binder.bind(BaseAuthService, to=AuthService)
        binder.bind(BaseWishListService, to=WishListService)
        binder.bind(BaseNotificationService, to=NotificationService)
