from dependency_injector import containers, providers

from api.data.sql.database import Database
from api.domain.models.todo_model import TodoModel
from api.domain.models.user_model import UserModel
from api.domain.repositories.todo_repository import TodoRepository
from api.domain.repositories.user_repository import UserRepository
from api.domain.schemas.todo import Todo
from api.domain.schemas.user import User


class RepositoryContainer(containers.DeclarativeContainer):
    database: Database = providers.Dependency()

    user_repository = providers.Factory(
        UserRepository,
        database=database,
        model=UserModel,
        schema=User
    )

    todo_repository = providers.Factory(
        TodoRepository,
        database=database,
        model=TodoModel,
        schema=Todo
    )