from abc import abstractmethod

from injector import inject

from app.models.notify import Notify
from app.models.user import User
from app.repositories.base_notify_repo import BaseNotifyRepo
from app.repositories.base_user_repo import BaseUserRepo
from app.unit_of_works.base_uow import BaseUOW


class BaseNotificationService:

    @inject
    def __init__(self, notify_repo: BaseNotifyRepo, user_repo: BaseUserRepo, uow: BaseUOW):
        raise NotImplementedError

    @abstractmethod
    def add_new_notify(self, notify: Notify) -> None:
        """
        新增通知
        Args:
            notify: 傳遞通知參數

        Returns: None

        """
        raise NotImplementedError

    @abstractmethod
    def get_user_settings(self, user: User) -> User:
        """
        取得使用者設定
        Args:
            user: 傳遞使用者參數

        Returns: 使用者設定

        """
        raise NotImplementedError

    @abstractmethod
    def edit_user_settings(self, user: User) -> None:
        """
        修改使用者設定
        Args:
            user: 傳遞使用者參數

        Returns: None

        """
        raise NotImplementedError
