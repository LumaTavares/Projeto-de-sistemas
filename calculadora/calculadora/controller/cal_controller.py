from fastapi import APIRouter,HTTPException
from calculadora.service import calculadora_service

router = APIRouter(prefix="/calculadora", tags=["calculadora"])

@router.get("/operacoes")
def get_operacoes():
    return {"operações":calculadora_service.listar_operacoes()}

@router.get("/{operacao}")
def calcular(operacao:str,a:float,b:float):
    try:
        resultado=calculadora_service.executar(operacao,a,b)
        return {"Operação":resultado}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

