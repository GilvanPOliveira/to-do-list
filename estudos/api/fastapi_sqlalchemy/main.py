from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./tarefas.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

class TarefaDB(Base):
    __tablename__ = "tarefas"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    descricao = Column(String)
    concluida = Column(Boolean, default=False)

class Tarefa(BaseModel):
    id: int | None = None
    titulo: str
    descricao: str
    concluida: bool = False

Base.metadata.create_all(bind=engine)

@app.get("/tarefas", response_model=List[Tarefa])
def listar():
    db = SessionLocal()
    tarefas = db.query(TarefaDB).all()
    db.close()
    return tarefas

@app.post("/tarefas", response_model=Tarefa)
def criar(tarefa: Tarefa):
    db = SessionLocal()
    nova = TarefaDB(**tarefa.dict(exclude={"id"}))
    db.add(nova)
    db.commit()
    db.refresh(nova)
    db.close()
    return nova

@app.put("/tarefas/{id}", response_model=Tarefa)
def atualizar(id: int, tarefa: Tarefa):
    db = SessionLocal()
    db_tarefa = db.query(TarefaDB).filter(TarefaDB.id == id).first()
    if not db_tarefa:
        db.close()
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    for k, v in tarefa.dict(exclude_unset=True).items():
        setattr(db_tarefa, k, v)
    db.commit()
    db.refresh(db_tarefa)
    db.close()
    return db_tarefa

@app.delete("/tarefas/{id}")
def deletar(id: int):
    db = SessionLocal()
    db_tarefa = db.query(TarefaDB).filter(TarefaDB.id == id).first()
    if not db_tarefa:
        db.close()
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    db.delete(db_tarefa)
    db.commit()
    db.close()
    return {"mensagem": f"Tarefa {id} deletada"}
