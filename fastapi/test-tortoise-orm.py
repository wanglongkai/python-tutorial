from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict
from tortoise import fields, models
from tortoise.contrib.fastapi import register_tortoise
from tortoise.exceptions import DoesNotExist

app = FastAPI()


# ── Models ──────────────────────────────────────────────────────────────────


class User(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100, unique=True)


# ── Schemas ─────────────────────────────────────────────────────────────────


class UserCreate(BaseModel):
    name: str
    email: str


class UserUpdate(BaseModel):
    name: str
    email: str


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: str


# ── DB setup ────────────────────────────────────────────────────────────────

register_tortoise(
    app,
    db_url="sqlite://data/test.db",
    modules={"models": ["__main__"]},
    generate_schemas=True,
)


# ── Routes ──────────────────────────────────────────────────────────────────


@app.post("/add_user", response_model=UserResponse)
async def add_user(body: UserCreate):
    user = await User.create(name=body.name, email=body.email)
    return user


@app.get("/users", response_model=list[UserResponse])
async def get_users():
    return await User.all()


@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    try:
        return await User.get(id=user_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="User not found")


@app.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, body: UserUpdate):
    try:
        user = await User.get(id=user_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="User not found")
    user.name = body.name
    user.email = body.email
    await user.save()
    return user


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    try:
        user = await User.get(id=user_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="User not found")
    await user.delete()
    return {"message": "User deleted successfully"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
