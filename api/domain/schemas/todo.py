from api.domain.schemas.schema_base import SchemaBase


class TodoBase(SchemaBase):
    description = str
    user_id = int


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    id: Optional[int] = None
    class Config:
        orm_mode = True


class TodoResponse(Todo):
    pass
