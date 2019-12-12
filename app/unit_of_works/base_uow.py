from abc import ABC, abstractmethod

from sqlalchemy.util.compat import contextmanager


class BaseUOW(ABC):

    @abstractmethod
    def complete(self):
        """
        完成後正式修改資料
        Returns: None

        """
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        """
        回復資料
        Returns: None

        """
        raise NotImplementedError

    @contextmanager
    def auto_complete(self):
        """
        自動完成資料的修改
        無錯誤 -> 正式修改資料
        有錯誤 -> 回復資料
        Returns: None

        """
        raise NotImplementedError
