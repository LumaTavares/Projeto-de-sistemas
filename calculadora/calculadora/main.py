from fastapi import FastAPI, APIRouter
from calculadora.controller.cal_controller import router

app =FastAPI()
app.include_router(router)

@app.get("/")
def inicio():
    return{"Mensagem":"calculadora"}