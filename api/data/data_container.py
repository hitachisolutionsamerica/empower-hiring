from dependency_injector import containers, providers

from api.data.sql.database import Database


class DataContainer(containers.DeclarativeContainer):
    app_config = providers.Dependency()

    database = providers.Factory(
        Database,
        app_config=app_config
    )