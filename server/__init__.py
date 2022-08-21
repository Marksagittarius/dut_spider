from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from starlette.requests import Request
from fastapi import FastAPI

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# 1. 题目1
@app.get("/actress")
async def render_actress_page(request: Request):
    return templates.TemplateResponse("actress.html", {"request": request})


# 2. 题目2
@app.get("/television")
async def render_television_page(request: Request):
    return templates.TemplateResponse("television.html", {"request": request})


@app.get("/epidemic")
async def render_epidemic_page(request: Request):
    return templates.TemplateResponse("epidemic.html", {"request": request})


def get_router():
    return app
