from pydantic import BaseModel

class OperacaoRequest(BaseModel):
    operacao:str
    a: float
    b: float