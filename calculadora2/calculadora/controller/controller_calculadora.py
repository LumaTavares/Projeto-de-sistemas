from fastapi import APIRouter,HTTPException
from calculadora.service import calculadora_service

router = APIRouter(prefix="/calculadora", tags=["calculadora"])

@router.get("/listar_operações")
def get_operacoes():
    return{"operações":calculadora_service.listar_ops()}

@router.get("/{op}")
def calcular(op: str, a: int, b: int):
    resultado = calculadora_service.executar(op, a, b)
    return {"resultado": resultado}