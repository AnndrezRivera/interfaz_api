import requests
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import pandas as pd

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "states": states, "categories": categories})

@app.post("/")
def index(request: Request, state: str = Form(...), categories: str = Form(...)):
    response = requests.get(f'https://api-recomendaciones.onrender.com/?state={state}&categoria={categories}')
    data = response.json()
    return templates.TemplateResponse("results.html", {"request": request, "results": data})

@app.get("/lugares_cercanos")
def sentimiento_index(request: Request):
    return templates.TemplateResponse("lugares_index.html", {"request": request, "states": states, "categories": categories})

@app.post("/lugares_cercanos")
def sentimiento_index(request: Request, state: str = Form(...), categories: str = Form(...)):
    response = requests.get(f'https://api-recomendaciones.onrender.com/lugares_cercanos?state={state}&categoria={categories}')
    data = response.json()
    return templates.TemplateResponse("lugares_results.html", {"request": request, "results": data})
