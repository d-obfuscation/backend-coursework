from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    context ={"request": request}
    return templates.TemplateResponse("./home/index.html", context)

@app.get("/books", response_class=HTMLResponse)
def index(request: Request):
    context ={"request": request}
    return templates.TemplateResponse("./books/books.html", context)

@app.get("/authors", response_class=HTMLResponse)
def index(request: Request):
    context ={"request": request}
    return templates.TemplateResponse("./authors/authors.html", context)