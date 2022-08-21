from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from starlette.requests import Request
from fastapi import FastAPI

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# Test1
@app.get("/actress")
async def render_actress_page(request: Request):
    return templates.TemplateResponse("actress.html", {"request": request})


# Test2
@app.get("/television")
async def render_television_page(request: Request):
    return templates.TemplateResponse("television.html", {"request": request})


# Test 3
@app.get("/epidemic")
async def render_epidemic_page(request: Request):
    return templates.TemplateResponse("epidemic.html", {"request": request})


def get_router():
    return app
