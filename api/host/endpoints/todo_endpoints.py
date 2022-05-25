from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from starlette import status

from api.domain.application_container import ApplicationContainer
from api.domain.schemas.todo import TodoCreate, Todo, TodoResponse
from api.host.endpoints.endpoints_base import EndpointsBase
from api.host.handler.todo_handler import TodoHandler

router = InferringRouter()


@cbv(router)
class TodoEndpoints(EndpointsBase[TodoCreate, Todo]):
    @inject
    def __init__(self,  handler: TodoHandler = Depends(Provide[ApplicationContainer.handler_container.todo_handler])):
        super().__init__(handler=handler)

    @router.post('/todos', status_code=status.HTTP_201_CREATED)
    def create(self, dto: TodoCreate) -> TodoResponse:
        result = super().create(dto)
        return result

    @router.get('/todos/{todo_id}')
    def get_by_id(self, todo_id: int) -> TodoResponse:
        result = super().get_by_id(todo_id)
        return result
