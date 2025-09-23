import inspect #pra usar reflection
from calculadora.models.operacoes import Operacoes


model = Operacoes()

def listar_operacoes():
    operacoes = []
    print("operações presentes na calculadora:")
    for name, obj in inspect.getmembers(Operacoes, inspect.isfunction):
        operacoes.append(name)
    return operacoes
def executar(operacao: str, a:float,b:float):
    if not hasattr(model,operacao):#verificar se objeto existe
        raise ValueError(f'Operação : {operacao} não existe') 
    metodo = getattr(model, operacao) #acessar o metodo dinamicamente 
    return metodo(a,b)