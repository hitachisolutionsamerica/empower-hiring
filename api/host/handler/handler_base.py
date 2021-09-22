from typing import TypeVar, Generic, Type

from api.core.util.json_helpers import JsonConvert
from api.domain.managers.manager_base import ManagerBase

from api.domain.models.model_base import ModelBase

TCreateSchema = TypeVar('TCreateSchema', bound=ModelBase)
TSchema = TypeVar('TSchema', bound=ModelBase)

# todo not sure if we need response here - might be handled by endpoints...
TResponse = TypeVar('TResponse', bound=ModelBase)


class HandlerBase(Generic[TCreateSchema, TSchema, TResponse]):
    def __init__(self, schema: Type[TSchema], manager: ManagerBase):
        self.manager = manager
        self.schema = schema

    def create(self, create_schema: TCreateSchema) -> TSchema:
        # todo: update generics/typing here...should be getting type hints...
        schema = JsonConvert.convert(create_schema, self.schema)

        result = self.manager.create(schema)
        return result

    def get_by_id(self, id: int) -> TSchema:
        result = self.manager.get_by_id(id)
        return result
