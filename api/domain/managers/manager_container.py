from dependency_injector import containers, providers

from api.domain.managers.todo_manager import TodoManager
from api.domain.managers.user_manager import UserManager


class ManagerContainer(containers.DeclarativeContainer):
    user_repository = providers.Dependency()
    todo_repository = providers.Dependency()

    user_manager = providers.Factory(
        UserManager,
        repository=user_repository
    )

    todo_manager = providers.Factory(
        TodoManager,
        repository=todo_repository
    )
