from api.domain.schemas.user import UserCreate, User, UserResponse
from api.host.handler.handler_base import HandlerBase


class UserHandler(HandlerBase[UserCreate, User, UserResponse]):
    pass