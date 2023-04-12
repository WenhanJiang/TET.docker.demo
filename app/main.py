from fastapi import FastAPI
from .import sqrt

app=FastAPI()

@app.get("/")
def index():
    return('hello data')
@app.post("/{number}")
def calculate(number:int):
    return sqrt(number)

