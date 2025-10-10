# app/routers/team.py
from fastapi import HTTPException
from sqlmodel import Session
from controller.generic import create_crud_router, Hooks
from model.models import Endereco, Pessoa 
from model.dto import EndCreate, EndUpdate, EndRead

class EnderecoHooks(Hooks[Endereco, EndUpdate, EndCreate]):
    def pre_create(self, payload: EndCreate, session: Session) -> None:
        """
        Antes de criar um Endereco, verifica se o pessoa_id é válido (se existir).
        """
        if payload.pessoa_id is not None:
            pessoa = session.get(Pessoa, payload.pessoa_id)
            if not pessoa:
                raise HTTPException(status_code=400, detail="pessoa_id inválido")

    def post_create(self, obj: Endereco, session: Session) -> None:
        """
        Depois de criar um Endereco, atualiza o campo end_id da Pessoa (se existir).
        """
        if obj.pessoa_id:
            pessoa = session.get(Pessoa, obj.pessoa_id)
            if pessoa:
                pessoa.end_id = obj.id
                session.add(pessoa)
                session.commit()
                session.refresh(pessoa)

    def pre_update(self, payload: EndUpdate, session: Session, obj: Endereco) -> None:
        """
        Antes de atualizar um Endereco, verifica se o pessoa_id informado (se existir) é válido.
        """
        if payload.pessoa_id is not None:
            pessoa = session.get(Pessoa, payload.pessoa_id)
            if not pessoa:
                raise HTTPException(status_code=400, detail="pessoa_id inválido")

    def post_update(self, obj: Endereco, session: Session) -> None:
        """
        Depois de atualizar um Endereco, atualiza o campo end_id da Pessoa (se necessário).
        """
        if obj.pessoa_id:
            pessoa = session.get(Pessoa, obj.pessoa_id)
            if pessoa and pessoa.end_id != obj.id:
                pessoa.end_id = obj.id
                session.add(pessoa)
                session.commit()
                session.refresh(pessoa)      

router = create_crud_router(
    model=Endereco,
    create_schema=EndCreate,
    update_schema=EndUpdate,
    read_schema=EndRead,
    prefix="/End",
    tags=["End"],
)