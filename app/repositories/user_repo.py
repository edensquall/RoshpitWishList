from app.models.user import User
from app.repositories.base_user_repo import BaseUserRepo
from app.repositories.generic_repo import GenericRepo


class UserRepo(GenericRepo[User], BaseUserRepo):

    def get_by_account(self, user: User) -> User:
        return User.query.filter_by(account=user.account).first()

    def get_by_account_and_password(self, user: User) -> User:
        return User.query.filter_by(account=user.account, password=user.password).first()
