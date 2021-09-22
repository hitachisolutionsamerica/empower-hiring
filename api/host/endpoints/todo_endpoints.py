from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from api.domain.schemas.todo import TodoCreate, Todo
from api.host.endpoints.endpoints_base import EndpointsBase

router = InferringRouter()


@cbv(router)
class TodoEndpoints(EndpointsBase[TodoCreate, Todo]):
    """Your code goes here"""
