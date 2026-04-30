from tortoise import fields, models
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()


register_tortoise(
    app,
    db_url="sqlite://data/test.db",
    modules={"models": ["__main__"]},
    generate_schemas=True,
)


class User(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100)


@app.post("/add_user")
async def add_user(name: str, email: str):
    user = await User.create(name=name, email=email)
    return user


@app.get("/users")
async def get_users():
    users = await User.all()
    return users


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = await User.get(id=user_id)
    return user


@app.put("/users/{user_id}")
async def update_user(user_id: int, name: str, email: str):
    user = await User.get(id=user_id)
    user.name = name
    user.email = email
    await user.save()
    return user


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    user = await User.get(id=user_id)
    await user.delete()
    return {"message": "User deleted successfully"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
