from typing import Optional, List

from api.domain.schemas.schema_base import SchemaBase
from api.domain.schemas.todo import Todo


class UserBase(SchemaBase):
    name: str
    age: Optional[int] = None


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: Optional[int] = None
    todos: List[Todo] = []

    class Config:
        orm_mode = True


class UserResponse(User):
    pass
