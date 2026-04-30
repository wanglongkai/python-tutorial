from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path

templates_dir = Path(__file__).resolve().parent.parent / "templates"
templates = Jinja2Templates(directory=str(templates_dir))

view_router = APIRouter(tags=["views"])


@view_router.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse(request, "login.html")
