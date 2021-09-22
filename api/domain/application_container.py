from dependency_injector import containers, providers

from api.config.app_config import AppConfig
from api.data.data_container import DataContainer
from api.domain.managers.manager_container import ManagerContainer
from api.domain.repositories.repository_container import RepositoryContainer
from api.host.handler.handler_container import HandlerContainer


class ApplicationContainer(containers.DeclarativeContainer):
    app_config = providers.Singleton(
        AppConfig
    )

    data_container: DataContainer = providers.Container(
        DataContainer,
        app_config=app_config
    )

    repository_container: RepositoryContainer = providers.Container(
        RepositoryContainer,
        database=data_container.database
    )

    manager_container: ManagerContainer = providers.Container(
        ManagerContainer,
        user_repository=repository_container.user_repository,
        todo_repository=repository_container.todo_repository
    )

    handler_container: HandlerContainer = providers.Container(
        HandlerContainer,
        user_manager=manager_container.user_manager,
        todo_manager=manager_container.todo_manager
    )