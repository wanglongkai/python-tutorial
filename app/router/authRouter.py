from fastapi import APIRouter, Depends
from utils.auth import create_access_token, get_payload_from_token
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/create_token")
async def create_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    access_token = create_access_token({"name": form_data.username})
    # 响应体中必须包含access_token字段
    return {"access_token": access_token, "token_type": "bearer"}


@auth_router.get("/get_payload")
async def get_payload(payload: dict = Depends(get_payload_from_token)):
    return payload
