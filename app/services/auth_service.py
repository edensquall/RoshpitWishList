from injector import inject

from app.models.user import User
from app.repositories.base_user_repo import BaseUserRepo
from app.services.base_auth_service import BaseAuthService
from app.unit_of_works.base_uow import BaseUOW


class AuthService(BaseAuthService):

    @inject
    def __init__(self, user_repo: BaseUserRepo, uow: BaseUOW):
        self.user_repo = user_repo
        self.uow = uow

    def register(self, user: User) -> None:
        with self.uow.auto_complete():
            self.user_repo.insert(user)

    def is_valid_login(self, user: User) -> bool:
        if self.user_repo.get_by_account_and_password(user):
            return True
        return False

    def get_user_by_account(self, user: User) -> User:
        return self.user_repo.get_by_account(user)
