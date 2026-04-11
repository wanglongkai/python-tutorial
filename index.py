from fastapi import Depends, FastAPI, Path, Query, HTTPException, Request
import uvicorn
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, FileResponse
from typing import Annotated

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def hello(
    name: str = Path(
        ..., min_length=3, max_length=10, description="The name of the person"
    )
):
    return {"message": f"Hello {name}"}


# 路径参数
@app.get("/items/{item_id}")
async def get_item(
    item_id: int = Path(..., description="The ID of the item", gt=0, lt=101)
):
    return {"item_id": item_id}


# 查询参数: 直接在处理函数中添加Query参数
@app.get("/news")
async def get_news(
    q: str = Query(
        "value",
        description="The query string",
        min_length=3,
        max_length=10,
        pattern="^[a-zA-Z0-9]+$",
    ),
    page: int = Query(1, description="The page number", gt=0),
    limit: int = Query(10, description="The number of items per page", gt=0, lt=101),
):
    return {"q": q, "page": page, "limit": limit}


# 请求体参数 : 1.使用Pydantic模型定义请求体 2.在处理函数中添加Body参数
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


@app.post("/items")
async def create_item(item: Item):
    return {"item": item}


@app.get("/html")
async def get_html():
    return HTMLResponse(content="<h1>Hello World</h1>", status_code=200)


@app.get("/file")
async def get_file():
    return FileResponse(path="pyproject.toml")


# 自定义响应数据格式
class CustomResponse(BaseModel):
    code: int
    message: str
    data: dict


@app.get("/custom", response_model=CustomResponse)
async def get_custom():
    return {"code": 200, "message": "success", "data": {"name": "John", "age": 20}}


# 异常处理
@app.get("/error")
async def get_error():
    raise HTTPException(status_code=400, detail="Bad Request")


# 中间件: 包裹应用，形成一个栈，从上往下，最后添加的中间件是“最外层”的，最先添加的是“最内层”的。
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


# 依赖注入
def get_db():
    return "Database Connection"


@app.get("/dependency")
async def get_dependency(db: Annotated[get_db, Depends()]):
    # 目前官方推荐Annotated[T, Depends(func)]的写法, 快捷写法是 Annotated[func, Depends()]
    return {"db": db}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
