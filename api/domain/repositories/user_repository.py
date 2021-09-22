from api.data.sql.sql_repository_base import SqlRepositoryBase
from api.domain.models.user_model import UserModel
from api.domain.schemas.user import User


class UserRepository(SqlRepositoryBase[UserModel, User]):
    pass
