from contextlib import contextmanager
from typing import Type

from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from api.config.app_config import AppConfig


class Database:
    def __init__(self, app_config: AppConfig) -> None:
        self._engine = create_engine(app_config.db_url, echo=True)
        self.session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine
            )
        )

    def create_database(self, base: Type[declarative_base]) -> None:
        base.metadata.create_all(self._engine)

    @contextmanager
    def session(self):
        session: Session = self.session_factory()
        try:
            yield session
        except Exception:
            # logger.exception(f'Session rollback due to exception: {Exception}')
            session.rollback()
            raise
        finally:
            session.close()
