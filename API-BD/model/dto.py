from typing import List, Optional
from sqlmodel import Field
from model.models import PessoaBase, EnderecoBase

# ----- Pessoa -----
class PessoaCreate(PessoaBase):
    pass

class PessoaUpdate(PessoaBase):
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None

class EndRead(EnderecoBase):
    id: int
    pessoa_id: Optional[int] = None
    model_config = {"from_attributes": True}
    
class PessoaRead(PessoaBase):
    id: int
    enderecos: List[EndRead] = []  # lista de endereços
    model_config = {"from_attributes": True}

# ----- Endereco -----
class EndCreate(EnderecoBase):
    pessoa_id: Optional[int] = None  

class EndUpdate(EnderecoBase):
    logradouro: Optional[str] = None
    numero: Optional[int] = None
    estado: Optional[str] = None
    cidade: Optional[str] = None
    bairro: Optional[str] = None

class EndPublic(EnderecoBase):
    id: int
    model_config = {"from_attributes": True}
