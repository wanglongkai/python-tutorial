# FastAPI
uvicorn是fastapi项目的运行环境，reload生效时，app实例应该传入字符串形式
```
uvicorn.run("main:app", port=8000, reload=True)
```