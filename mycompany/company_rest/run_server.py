from fastapi import FastAPI
import uvicorn

from company_rest.routes import position, worker, department, skill


def prepare_application():
    app = FastAPI()
    app.include_router(position.router)
    app.include_router(worker.router)
    app.include_router(department.router)
    app.include_router(skill.router)
    return app


def run_server():
    app = prepare_application()
    uvicorn.run(
        app,
        host="0.0.0.0"
        # port=config.port,
    )
