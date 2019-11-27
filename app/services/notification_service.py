from injector import inject

from app.models.notify import Notify
from app.models.user import User
from app.repositories.base_notify_repo import BaseNotifyRepo
from app.repositories.base_user_repo import BaseUserRepo
from app.services.base_notification_service import BaseNotificationService
from app.unit_of_works.base_uow import BaseUOW


class NotificationService(BaseNotificationService):

    @inject
    def __init__(self, notify_repo: BaseNotifyRepo, user_repo: BaseUserRepo, uow: BaseUOW):
        self.notify_repo = notify_repo
        self.user_repo = user_repo
        self.uow = uow

    def add_new_notify(self, notify: Notify) -> None:
        with self.uow.auto_complete():
            self.notify_repo.insert(notify)

    def get_user_settings(self, user: User) -> User:
        return self.user_repo.get_by_id(user)

    def edit_user_settings(self, user: User) -> None:
        with self.uow.auto_complete():
            self.user_repo.insert(user)

