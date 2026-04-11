from fastapi import FastAPI
from router.userRouter import user_router
from router.newsRouter import news_router
from db.dbconfig import handle_tortoise

app = FastAPI()

app.include_router(user_router)
app.include_router(news_router)


handle_tortoise(app)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
