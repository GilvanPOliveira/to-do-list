from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas
from app.auth import obter_usuario_atual
from app.models import User
from typing import List

router = APIRouter(
    prefix="/tarefas",
    tags=["Tarefas"]
)

@router.post("/", response_model=schemas.TaskOut)
def criar_tarefa(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(obter_usuario_atual)
):
    return crud.criar_task(db=db, task=task, user_id=current_user.id)

@router.get("/", response_model=List[schemas.TaskOut])
def listar_tarefas(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(obter_usuario_atual)
):
    return crud.listar_tasks(db=db, skip=skip, limit=limit, user_id=current_user.id)

@router.get("/{task_id}", response_model=schemas.TaskOut)
def obter_tarefa(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(obter_usuario_atual)
):
    db_task = crud.obter_task(db=db, task_id=task_id, user_id=current_user.id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return db_task

@router.put("/{task_id}", response_model=schemas.TaskOut)
def atualizar_tarefa(
    task_id: int,
    task: schemas.TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(obter_usuario_atual)
):
    db_task = crud.atualizar_task(db=db, task_id=task_id, task=task, user_id=current_user.id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return db_task

@router.delete("/{task_id}", status_code=204)
def deletar_tarefa(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(obter_usuario_atual)
):
    sucesso = crud.deletar_task(db=db, task_id=task_id, user_id=current_user.id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return None
