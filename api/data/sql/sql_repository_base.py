from abc import ABC
from typing import TypeVar, Generic, Type

import pydantic
from fastapi import Query
from fastapi.encoders import jsonable_encoder

from api.data.sql.database import Database
from api.domain.models.model_base import ModelBase

TModel = TypeVar('TModel', bound=ModelBase)
TSchema = TypeVar('TSchema', bound=pydantic.BaseModel)


class SqlRepositoryBase(Generic[TModel, TSchema], ABC):
    def __init__(self, database: Database, model: Type[TModel], schema: Type[TSchema]):
        self.__database = database
        self.__session_factory = self.__database.session_factory
        self.model = model
        self.schema = schema

    def create(self, entity: TSchema) -> TSchema:
        entity_data = jsonable_encoder(entity, by_alias=False)
        model = self.model(**entity_data)

        with self.__session_factory() as session:
            session.add(model)
            session.commit()
            session.refresh(model)

        model_data = jsonable_encoder(model)
        saved_entity = self.schema(**model_data)
        return saved_entity

    def get_by_id(self, id: int):
        with self.__session_factory() as session:
            model = session.query(self.model).filter(self.model.id == id).first()
        return model
