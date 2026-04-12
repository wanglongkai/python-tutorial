from fastapi import FastAPI, Request
from router.userRouter import user_router
from router.authRouter import auth_router
from config.dbconfig import handle_tortoise
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from config.redisconfig import redis_connect


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 在应用启动时执行
    print("Starting up...", app.title)
    # 将redis连接保存到应用状态中
    app.state.redis = await redis_connect()
    yield
    # 在应用关闭时执行
    print("Shutting down...", app.title)
    # 关闭redis连接
    if app.state.redis:
        await app.state.redis.close()


app = FastAPI(lifespan=lifespan, title="FastAPI Tutorial")


# 中间件: 包裹应用，形成一个类似于洋葱模型的结构，最后添加的中间件是“最外层”的，最先添加的是“最内层”的。
@app.middleware("http")
async def middleware1(request: Request, call_next):
    print(f"Request1: {request.url}")
    response = await call_next(request)
    print(f"Response1: {response.status_code}")
    return response


@app.middleware("http")
async def middleware2(request: Request, call_next):
    print(f"Request2: {request.url}")
    response = await call_next(request)
    print(f"Response2: {response.status_code}")
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)
app.include_router(user_router)


handle_tortoise(app)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
