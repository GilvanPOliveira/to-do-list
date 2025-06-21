from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .models import Tarefa, User
from .schemas import TarefaCreate, TarefaOut
from .database import get_db
from .auth import verificar_token_jwt
from typing import List

router = APIRouter()

@router.post("/tarefas/", response_model=TarefaOut)
def criar_tarefa(tarefa: TarefaCreate, db: Session = Depends(get_db), usuario_id: int = Depends(verificar_token_jwt)):
    nova_tarefa = Tarefa(titulo=tarefa.titulo, descricao=tarefa.descricao, feita=False, usuario_id=usuario_id)
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)
    return nova_tarefa

@router.get("/tarefas/", response_model=List[TarefaOut])
def listar_tarefas(db: Session = Depends(get_db), usuario_id: int = Depends(verificar_token_jwt)):
    return db.query(Tarefa).filter(Tarefa.usuario_id == usuario_id).all()
