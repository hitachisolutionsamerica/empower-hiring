from pydantic import BaseModel

from api.core.util.string_helpers import snake_to_pascal


class SchemaBase(BaseModel):
    class Config:
        alias_generator = snake_to_pascal
        allow_population_by_field_name = True
