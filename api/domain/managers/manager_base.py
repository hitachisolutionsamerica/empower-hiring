from abc import ABC
from typing import TypeVar, Generic

import pydantic

from api.data.sql.sql_repository_base import SqlRepositoryBase

TSchema = TypeVar('TSchema', bound=pydantic.BaseModel)


class ManagerBase(Generic[TSchema], ABC):
    def __init__(self, repository: SqlRepositoryBase):
        self.repository = repository

    def create(self, entity: TSchema) -> TSchema:
        # business logic validation
        result = self.repository.create(entity)
        return result

    def get_by_id(self, id: int):
        result = self.repository.get_by_id(id)
        return result
