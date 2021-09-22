from dependency_injector import containers, providers

from api.domain.schemas.todo import Todo
from api.domain.schemas.user import User
from api.host.handler.todo_handler import TodoHandler
from api.host.handler.user_handler import UserHandler


class HandlerContainer(containers.DeclarativeContainer):
    user_manager = providers.Dependency()
    todo_manager = providers.Dependency()


    user_handler = providers.Factory(
        UserHandler,
        schema=User,
        manager=user_manager
    )

    todo_handler = providers.Factory(
        TodoHandler,
        schema=Todo,
        manager=todo_manager
    )

