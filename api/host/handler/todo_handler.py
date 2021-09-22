from api.domain.schemas.todo import TodoResponse, Todo, TodoCreate
from api.host.handler.handler_base import HandlerBase


class TodoHandler(HandlerBase[TodoCreate, Todo, TodoResponse]):
    pass
