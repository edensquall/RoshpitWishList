from abc import abstractmethod

from injector import inject

from app.models.user import User
from app.repositories.base_user_repo import BaseUserRepo
from app.unit_of_works.base_uow import BaseUOW


class BaseAuthService:

    @inject
    def __init__(self, user_repo: BaseUserRepo, uow: BaseUOW):
        raise NotImplementedError

    @abstractmethod
    def register(self, user: User) -> None:
        """
        註冊使用者
        Args:
            user: 傳遞使用者參數

        Returns: None

        """
        raise NotImplementedError

    @abstractmethod
    def is_valid_login(self, user: User) -> bool:
        """
        檢查登入是否正確
        Args:
            user: 傳遞使用者參數

        Returns: 登入是否正確

        """
        raise NotImplementedError

    @abstractmethod
    def get_user_by_account(self, user: User) -> User:
        """
        取得某個帳號的使用者
        Args:
            user: 傳遞使用者參數

        Returns: 某個帳號的使用者

        """
        raise NotImplementedError
