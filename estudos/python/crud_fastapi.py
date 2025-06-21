from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class Tarefa(BaseModel):
    id: int
    titulo: str
    descricao: str
    concluida: bool = False

tarefas: List[Tarefa] = []
proximo_id = 1

@app.get("/tarefas")
def listar_tarefas():
    return tarefas

@app.post("/tarefas")
def criar_tarefa(tarefa: Tarefa):
    global proximo_id
    tarefa.id = proximo_id
    tarefas.append(tarefa)
    proximo_id += 1
    return tarefa

@app.put("/tarefas/{id}")
def atualizar_tarefa(id: int, nova: Tarefa):
    for i, t in enumerate(tarefas):
        if t.id == id:
            tarefas[i] = nova
            return nova
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@app.delete("/tarefas/{id}")
def deletar_tarefa(id: int):
    global tarefas
    tarefas = [t for t in tarefas if t.id != id]
    return {"mensagem": f"Tarefa {id} removida"}