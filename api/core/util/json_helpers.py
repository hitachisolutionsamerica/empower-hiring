from typing import TypeVar, Type

import pydantic
from fastapi.encoders import jsonable_encoder

from api.domain.models.model_base import ModelBase

TModel = TypeVar('TModel', bound=ModelBase)
TSchema = TypeVar('TSchema', bound=pydantic.BaseModel)

TInput = TypeVar('TInput')
TOutput = TypeVar('TOutput')


class JsonConvert:
    @staticmethod
    def model_to_schema(obj_in: TModel, output_type: Type[TSchema]) -> TSchema:
        return JsonConvert.__convert(obj_in, output_type)

    @staticmethod
    def schema_to_model(obj_in: TSchema, output_type: Type[TModel]) -> TModel:
        return JsonConvert.__convert(obj_in, output_type)

    @staticmethod
    def convert(obj_in: TInput, output_type: Type[TOutput]) -> TOutput:
        return JsonConvert.__convert(obj_in, output_type)

    @staticmethod
    def __convert(obj_in, output_type):
        input_data = jsonable_encoder(obj_in, by_alias=False)
        output = output_type(**input_data)
        return output
