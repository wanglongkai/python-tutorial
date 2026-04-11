from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI


def handle_tortoise(app: FastAPI):
    register_tortoise(
        app,
        db_url="sqlite://users.db",
        modules={"models": ["models.userModel"]},
        generate_schemas=True,
    )
