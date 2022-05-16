from api.domain.schemas.schema_base import SchemaBase

from typing import Optional

class TodoBase(SchemaBase):
    """your code goes here"""
    description: str
    user_id: Optional[int] = None


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class TodoResponse(Todo):
    pass
