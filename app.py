from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

states = df['state'].unique().tolist()
categories = df['categories'].str.split(', ').explode().unique().tolist()

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "states": states, "categories": categories})

@app.post("/")
def index(request: Request, state: str = Form(...), categoria: str = Form(...)):
    response = requests.get(f'https://api-recomendaciones.onrender.com/?state={state}&categoria={categoria}')
    data = response.json()
    return templates.TemplateResponse("results.html", {"request": request, "results": data})

@app.get("/sentimiento_cercano")
def sentimiento_index(request: Request):
    return templates.TemplateResponse("sentimiento_index.html", {"request": request, "states": states, "categories": categories})

@app.post("/sentimiento_cercano")
def sentimiento_index(request: Request, state: str = Form(...), categoria: str = Form(...)):
    response = requests.get(f'https://api-recomendaciones.onrender.com/sentimiento_cercano?state={state}&categoria={categoria}')
    data = response.json()
    return templates.TemplateResponse("sentimiento_results.html", {"request": request, "results": data})
