from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
import requests
import pandas as pd

app = FastAPI()
templates = Jinja2Templates(directory="templates")

df1 = pd.read_parquet('dataset/archivo1.parquet')
df2 = pd.read_parquet('dataset/archivo2.parquet')
df = pd.concat([df1, df2])

us_states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
states = df[df['state'].isin(us_states)]['state'].unique().tolist()
categories = input()


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

