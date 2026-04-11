"""
schemas 定义数据格式校验， 基于pydantic库
"""

from pydantic import BaseModel


class RegisterUser(BaseModel):
    name: str
    email: str
    phone: str
