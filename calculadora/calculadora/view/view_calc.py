from fastapi import APIRouter, HTTPException
from calculadora.controllers import calc_controller

router = APIRouter()

@router.get("/")
def inicio():
    return{"Mensagem":"calculadora"}

@router.get("/operacoes")
def get_operacoes():
    return {"operações":calc_controller.listar_operacoes()}

@router.get("/{operacao}")
def calcular(operacao:str,a:float,b:float):
    try:
        resultado=calc_controller.executar(operacao,a,b)
        return {"Operação":resultado}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
