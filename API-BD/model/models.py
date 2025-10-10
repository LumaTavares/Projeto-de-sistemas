from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

#classe base para Pessoa - contém os campos comuns de uma pessoa. 
class PessoaBase(SQLModel):
    name: str
    age: int = Field(ge=0, le=120)
    email: str

class Pessoa(PessoaBase, table=True): #representa a tabela pessoa no banco
    id: Optional[int] = Field(default=None, primary_key=True)
    enderecos: List["Endereco"] = Relationship(back_populates="pessoa")

class EnderecoBase(SQLModel):
    logradouro: str
    numero: int
    estado: str
    cidade: str
    bairro: str

class Endereco(EnderecoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    pessoa_id: Optional[int] = Field(default=None, foreign_key="pessoa.id")
    pessoa: Optional[Pessoa] = Relationship(back_populates="enderecos")
