from abc import ABC
from typing import TypeVar, Generic

from api.domain.schemas.schema_base import SchemaBase
from api.host.handler.handler_base import HandlerBase

TCreate = TypeVar('TCreate', bound=SchemaBase)
TDefault = TypeVar('TDefault', bound=SchemaBase)


class EndpointsBase(Generic[TCreate, TDefault], ABC):
    def __init__(self, handler: HandlerBase):
        self.handler = handler

    def create(self, schema: TCreate) -> TDefault:
        result = self.handler.create(schema)
        return result

    def get_by_id(self, id: int) -> TDefault:
        result = self.handler.get_by_id(id)
        return result
