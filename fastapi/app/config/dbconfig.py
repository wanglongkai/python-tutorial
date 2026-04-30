from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI


def handle_tortoise(app: FastAPI):
    register_tortoise(
        app,
        db_url="sqlite://data/users.db",
        modules={"models": ["fastapi.app.models.userModel"]},
        generate_schemas=True,
    )
