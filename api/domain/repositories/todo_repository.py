from api.data.sql.sql_repository_base import SqlRepositoryBase
from api.domain.models.todo_model import TodoModel
from api.domain.schemas.todo import Todo


class TodoRepository(SqlRepositoryBase[TodoModel, Todo]):
    pass
