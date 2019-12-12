from abc import abstractmethod

from app.models.user import User
from app.repositories.base_repo import BaseRepo


class BaseUserRepo(BaseRepo[User]):

    @abstractmethod
    def get_by_account(self, user: User) -> User:
        """
        取得某個帳號的使用者
        Args:
            user: 傳遞使用者參數

        Returns: 某個帳號的使用者

        """
        raise NotImplementedError

    @abstractmethod
    def get_by_account_and_password(self, user: User) -> User:
        """
        取得某個帳號與密碼的使用者
        Args:
            user: 傳遞使用者參數

        Returns: 某個帳號與密碼的使用者

        """
        raise NotImplementedError
