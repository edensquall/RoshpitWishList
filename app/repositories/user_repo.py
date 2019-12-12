from app.models.user import User
from app.repositories.base_user_repo import BaseUserRepo
from app.repositories.generic_repo import GenericRepo


class UserRepo(GenericRepo[User], BaseUserRepo):

    def get_by_account(self, user: User) -> User:
        """
        取得某個帳號的使用者
        Args:
            user: 傳遞使用者參數

        Returns: 某個帳號的使用者

        """
        return User.query.filter_by(account=user.account).first()

    def get_by_account_and_password(self, user: User) -> User:
        """
        取得某個帳號與密碼的使用者
        Args:
            user: 傳遞使用者參數

        Returns: 某個帳號與密碼的使用者

        """
        return User.query.filter_by(account=user.account, password=user.password).first()
