#apresentar os dados
from calculadora.model.calculadora_operacoes import operacoes
import inspect
op = operacoes()
def listar_ops():
    i=0
    opcoes = {}
    for name,value in inspect.getmembers(op,inspect.ismethod):
        i+=1
        print(f"{i}->{name}")
        opcoes[str(i)]=name#dicionario com as operações
    return opcoes

def executar(operacao: str, a: int, b: int):
    nome_operacao=operacao.lower()  
    if b==0:
        raise ValueError(f"divisão por zero")
    if hasattr(op, nome_operacao): #retorna True se tiver a operação
        metodo = getattr(op, nome_operacao)
        return metodo(a, b)
    else:
        raise ValueError("Operação não existe")
    
   