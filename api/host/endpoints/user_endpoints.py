from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from starlette import status

from api.domain.application_container import ApplicationContainer
from api.domain.schemas.user import UserCreate, User, UserResponse
from api.host.endpoints.endpoints_base import EndpointsBase
from api.host.handler.user_handler import UserHandler

router = InferringRouter()


@cbv(router)
class UserEndpoints(EndpointsBase[UserCreate, User]):
    @inject
    def __init__(self,  handler: UserHandler = Depends(Provide[ApplicationContainer.handler_container.user_handler])):
        super().__init__(handler=handler)

    @router.post('/users', status_code=status.HTTP_201_CREATED)
    def create(self, dto: UserCreate) -> UserResponse:
        result = super().create(dto)
        return result

    @router.get('/users/{user_id}')
    def get_by_id(self, user_id: int) -> UserResponse:
        result = super().get_by_id(user_id)
        return result