from abc import abstractmethod

from app.models.user import User
from app.repositories.base_repo import BaseRepo


class BaseUserRepo(BaseRepo[User]):

    @abstractmethod
    def get_by_account(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    def get_by_account_and_password(self, user: User) -> User:
        raise NotImplementedError
