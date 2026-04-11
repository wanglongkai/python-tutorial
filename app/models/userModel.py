"""
models 定义数据模型， 基于tortoise-orm库
"""

from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100)
    phone = fields.CharField(max_length=100)
