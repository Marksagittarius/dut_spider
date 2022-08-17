from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from starlette.requests import Request
from fastapi import FastAPI
    
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/actress")
async def render_actress_page(request: Request):
    return templates.TemplateResponse("actress.html", {"request": request})


@app.get("/television")
async def render_television_page(request: Request):
    return templates.TemplateResponse("television.html", {"request": request})


def get_router():
    return app
