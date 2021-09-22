from api.domain.schemas.schema_base import SchemaBase


class TodoBase(SchemaBase):
    """your code goes here"""


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    class Config:
        orm_mode = True


class TodoResponse(Todo):
    pass
