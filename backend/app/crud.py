from sqlalchemy.orm import Session
from typing import List, Optional
from app import schemas
from . import models

def listar_tasks(db: Session, skip: int = 0, limit: int = 100, user_id: int = None) -> List[models.Task]:
    query = db.query(models.Task)
    if user_id is not None:
        query = query.filter(models.Task.user_id == user_id)
    return query.offset(skip).limit(limit).all()

def criar_task(db: Session, task: schemas.TaskCreate, user_id: int) -> models.Task:
    nova_task = models.Task(**task.model_dump(), user_id=user_id)
    db.add(nova_task)
    db.commit()
    db.refresh(nova_task)
    return nova_task


def obter_task(db: Session, task_id: int, user_id: int) -> Optional[models.Task]:
    return db.query(models.Task).filter(models.Task.id == task_id, models.Task.user_id == user_id).first()

def atualizar_task(db: Session, task_id: int, task: schemas.TaskUpdate, user_id: int) -> Optional[models.Task]:
    db_task = db.query(models.Task).filter(models.Task.id == task_id, models.Task.user_id == user_id).first()
    if db_task:
        for campo, valor in task.model_dump(exclude_unset=True).items():
            setattr(db_task, campo, valor)
        db.commit()
        db.refresh(db_task)
    return db_task

def deletar_task(db: Session, task_id: int, user_id: int) -> bool:
    db_task = db.query(models.Task).filter(models.Task.id == task_id, models.Task.user_id == user_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
        return True
    return False
