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
        raise NotImplementedError

    @abstractmethod
    def is_valid_login(self, user: User) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_user_by_account(self, user: User) -> User:
        raise NotImplementedError
