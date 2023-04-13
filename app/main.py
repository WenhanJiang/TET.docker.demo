from fastapi import FastAPI
from .mysqrt import sqrt

app=FastAPI()

@app.get("/")
def index():
    return('hello data')
@app.get("/sqrt/{number}")
def calculate(number:int):
    return {sqrt(number)}

