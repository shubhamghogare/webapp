from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Numbers(BaseModel):
    num1: float
    num2: float

@app.post("/addition")
def addition(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {"result": result}

@app.post("/multiplication")
def multiplication(numbers: Numbers):
    result = numbers.num1 * numbers.num2
    return {"result": result}

@app.post("/subtraction")
def subtraction(numbers: Numbers):
    result = numbers.num1 - numbers.num2
    return {"result": result}
