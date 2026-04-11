from fastapi import APIRouter

news_router = APIRouter(prefix="/news", tags=["news"])


@news_router.get("/")
async def get_news():
    return {"message": "新闻路由分组"}
