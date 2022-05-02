from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from api.domain.schemas.todo import TodoCreate, Todo
from api.host.endpoints.endpoints_base import EndpointsBase

router = InferringRouter()


@cbv(router)
class TodoEndpoints(EndpointsBase[TodoCreate, Todo]):
     @inject
    def __init__(self,  handler: TodoHandler = Depends(Provide[ApplicationContainer.handler_container.TodoHandler])):
        super().__init__(handler=handler)

    @router.post('/todo', status_code=status.HTTP_201_CREATED)
    def create(self, dto: TodoCreate) -> TodoResponse:
        result = super().create(dto)
        return result

    @router.get('/todo/{todo_id}')
    def get_by_id(self, todo_id: int) -> TodoResponse:
        result = super().get_by_id(todo_id)
        return result
