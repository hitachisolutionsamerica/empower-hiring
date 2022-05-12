from fastapi import Depends, HTTPException
from starlette import status
from fastapi_utils.cbv import cbv
from dependency_injector.wiring import Provide, inject
from fastapi_utils.inferring_router import InferringRouter

from typing import Union, Type
from api.domain.schemas.todo import TodoCreate, Todo
from api.host.handler.todo_handler import TodoHandler
from api.host.endpoints.endpoints_base import EndpointsBase
from api.domain.application_container import ApplicationContainer
from api.domain.schemas.todo import TodoCreate, Todo, TodoResponse

router = InferringRouter()


@cbv(router)
class TodoEndpoints(EndpointsBase[TodoCreate, Todo]):
    """Your code goes here"""
    @inject
    def __init__(self,  handler: TodoHandler = Depends(Provide[ApplicationContainer.handler_container.todo_handler])):
        super().__init__(handler=handler)


    @router.post('/todos', status_code = status.HTTP_201_CREATED)
    def create(self, dto: TodoCreate) -> TodoResponse:
        result = super().create(dto)
        return result

    @router.get('/todos/{todo_id}')
    def get_by_id(self, todo_id: int):
        result = super().get_by_id(todo_id)
        if result is None:
            return HTTPException(status_code=404, detail=f'Record with id -> {todo_id} not found.')
        return result

    @router.delete('/todos/{todo_id}')
    def delete_by_id(self, todo_id: int):
        if super().get_by_id(todo_id) is None:
            return HTTPException(status_code=404, detail=f'Record with id -> {todo_id} not found.')
        result = super().delete(todo_id)
        return result