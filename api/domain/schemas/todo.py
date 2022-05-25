from typing import Optional

from api.domain.schemas.schema_base import SchemaBase


class TodoBase(SchemaBase):
    description: str

class TodoCreate(TodoBase):
    user_id: int


class Todo(TodoBase):
    id: Optional[int] = None
    user_id: int
    
    class Config:
        orm_mode = True

class TodoResponse(Todo):
    pass
