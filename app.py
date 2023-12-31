import requests
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import pandas as pd

app = FastAPI()
templates = Jinja2Templates(directory="templates")


states = ['WA', 'LA', 'IL', 'OH', 'TN', 'CO', 'CA', 'MO', 'SC', 'NC', 'FL', 'TX', 'PA', 'NY', 'ND', 'VA', 'NE', 'MN', 'NH', 'UT', 'OR', 'GA', 'OK', 'NJ', 'AR', 'DE', 'AL', 'ME', 'MI', 'MA', 'AZ', 'CT', 'WI', 'IN', 'KY', 'AK', 'NM', 'MD', 'NV', 'WY', 'RI', 'IA', 'SD', 'VT', 'MS', 'KS', 'HI', 'WV', 'MT', 'ID', 'AB']


categories = ['burger', 'burgers', 'hamburger', 'hamburgers', 'hot dog', 'steakhouse', 'lunch', 'motel', 'patisserie', 'pizza', 'deli', 'diner', 'dinner', 'icecream', 'ice cream', 'hotel', 'hotels', 'seafood', 'cookie', 'crab house', 'cupcake', 'chocolate', 'churreria', 'cocktail', 'cocktails', 'coffee', 'coffees', 'tea', 'restaurant', 'restaurats', 'cheese', 'charcuterie', 'cafe', 'cafes', 'BBQ', 'bagel', 'bakery', 'bakerys', 'bar', 'bars', 'bar & grill', 'barbecue', 'beer', 'bistro', 'pastry shop', 'pastry shops', 'breakfast', 'brunch', 'buffet', 'burrito', 'cafeteria', 'cafeterias', 'cake', 'cakes', 'food', 'wine', 'wineries']


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
