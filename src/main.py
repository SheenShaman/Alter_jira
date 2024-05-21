from typing import Union

from fastapi import FastAPI

from src.api.person import person_router
from src.config.settings import AppSettings

app = FastAPI(**AppSettings().model_dump())

app.include_router(person_router)


@app.on_event("startup")
async def startup_event():
    from src.config.db import Base, engine
    from src.models.person import Person
    from src.models.task import Task

    Base.metadata.create_all(bind=engine)


# app = FastAPI()
#
#
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


