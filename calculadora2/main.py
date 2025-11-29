from fastapi import FastAPI, APIRouter
from calculadora.controller.controller_calculadora import router

app =FastAPI()
app.include_router(router)

@app.get("/")
def inicio():
    return{"Mensagem":"calculadora"}