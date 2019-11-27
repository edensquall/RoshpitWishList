from abc import ABC, abstractmethod
from typing import TypeVar, Generic

DTO = TypeVar('DTO')
Model = TypeVar('Model')


class BaseMapper(ABC, Generic[DTO, Model]):

    @abstractmethod
    def to_model(self, dto: DTO) -> Model:
        raise NotImplementedError

    @abstractmethod
    def to_dto(self, model: Model) -> DTO:
        raise NotImplementedError
