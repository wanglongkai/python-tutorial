import json
from typing import Any
import redis.asyncio as redis

redis_pool = redis.ConnectionPool(
    host="localhost",
    port=6379,
    decode_responses=True,
    encoding="utf-8",
)


redis_client = None


async def redis_connect() -> redis.Redis:
    try:
        redis_clinet = redis.Redis(connection_pool=redis_pool)
        sig = await redis_clinet.ping()
        print(f"连接redis成功: {sig}")
        return redis_clinet
    except Exception as e:
        print(f"连接redis失败: {e}")
        return None


"""
封装redis的设置和读取方法
"""


# 读取字符串缓存
async def get_str_cache(key: str) -> str:
    try:
        return await redis_client.get(key)
    except Exception as e:
        print(f"读取字符串缓存失败: {e}")
        return None


# 读取json缓存
async def get_json_cache(key: str) -> dict:
    try:
        value = await redis_client.get(key)
        if value:
            return json.loads(value)
        return None
    except Exception as e:
        print(f"读取json缓存失败: {e}")
        return None


# 设置缓存 避免大量key同时过期，导致缓存雪崩
async def set_cache(key: str, value: Any, expire_time: int = 60 * 60 * 24 * 7):
    try:
        if isinstance(value, (list, dict)):
            value = json.dumps(
                value, ensure_ascii=False
            )  # 确保json字符串不包含ascii字符
        await redis_client.setex(key, expire_time, value)
        return True
    except Exception as e:
        print(f"设置缓存失败: {e}")
        return False
