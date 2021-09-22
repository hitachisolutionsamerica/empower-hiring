import sys

from fastapi import FastAPI
import uvicorn

import api
from api.domain.application_container import ApplicationContainer
from api.domain.models.user_model import UserModel
from api.host.endpoints.user_endpoints import router as user_router
from api.host.endpoints.todo_endpoints import router as todo_router


def create_app() -> FastAPI:
    container = ApplicationContainer()
    # container.config.from_yaml('config.yml')
    container.wire(modules=[sys.modules[__name__]])
    container.wire(packages=[api.host.endpoints])

    db = container.data_container.database()
    db.create_database(base=UserModel)

    app = FastAPI()
    app.include_router(user_router)
    app.include_router(todo_router)
    app.container = container
    return app


app = create_app()

if __name__ == '__main__':
    uvicorn.run("api.main:app", host="0.0.0.0", port=8080, reload=True, access_log=False)
