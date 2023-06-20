from fastapi import FastAPI, Form
from fastapi import Request
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/")
def index(request: Request, state: str = Form(...), categoria: str = Form(...)):
    response = requests.get(f'https://api-recomendaciones.onrender.com/?state={state}&categoria={categoria}')
    data = response.json()
    return templates.TemplateResponse("results.html", {"request": request, "results": data})

