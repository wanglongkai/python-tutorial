from fastapi import APIRouter
from ..models.userModel import User
from ..crud.userCrud import get_all_users
from ..schemas.registerUser import RegisterUser

user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.post("/register")
async def register(user: RegisterUser):
    user = await User.create(name=user.name, email=user.email, phone=user.phone)
    return {"message": "User registered successfully", "user": user}


@user_router.post("/add_user")
async def add_user(name: str, email: str, phone: str):
    user = await User.create(name=name, email=email, phone=phone)
    return user


@user_router.get("/users")
async def get_users():
    users = await get_all_users()
    return users


@user_router.get("/users/{user_id}")
async def get_user(user_id: int):
    user = await User.get(id=user_id)
    return user


@user_router.put("/users/{user_id}")
async def update_user(user_id: int, name: str, email: str):
    user = await User.get(id=user_id)
    user.name = name
    user.email = email
    await user.save()
    return user


@user_router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    user = await User.get(id=user_id)
    await user.delete()
    return {"message": "User deleted successfully"}
