from fastapi import FastAPI
from calculadora.view import view_calc

app =FastAPI()

app.include_router(view_calc.router)