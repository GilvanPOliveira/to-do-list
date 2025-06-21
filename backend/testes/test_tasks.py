import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def token_valido():
    client.post("/register", json={"email": "user2@example.com", "password": "senha123"})
    resposta = client.post("/login", json={"email": "user2@example.com", "senha": "senha123"})
    return resposta.json()["access_token"]

@pytest.fixture
def tarefa_criada(token_valido):
    resposta = client.post(
        "/tarefas/",
        json={"titulo": "Tarefa Inicial", "descricao": "Teste"},
        headers={"Authorization": f"Bearer {token_valido}"}
    )
    return resposta.json()["id"]

def test_criar_tarefa(token_valido):
    resposta = client.post(
        "/tarefas/",
        json={"titulo": "Tarefa Teste", "descricao": "Descrição da tarefa"},
        headers={"Authorization": f"Bearer {token_valido}"}
    )
    assert resposta.status_code == 200
    assert resposta.json()["titulo"] == "Tarefa Teste"

def test_listar_tarefas(token_valido):
    resposta = client.get("/tarefas/", headers={"Authorization": f"Bearer {token_valido}"})
    assert resposta.status_code == 200
    assert isinstance(resposta.json(), list)

def test_atualizar_tarefa(token_valido, tarefa_criada):
    resposta = client.put(
        f"/tarefas/{tarefa_criada}",
        json={"titulo": "Atualizada", "descricao": "Editada", "concluida": True},
        headers={"Authorization": f"Bearer {token_valido}"}
    )
    assert resposta.status_code == 200
    assert resposta.json()["titulo"] == "Atualizada"
    assert resposta.json()["concluida"] is True

def test_deletar_tarefa(token_valido, tarefa_criada):
    resposta = client.delete(
        f"/tarefas/{tarefa_criada}",
        headers={"Authorization": f"Bearer {token_valido}"}
    )
    assert resposta.status_code == 204

def test_sem_token():
    resposta = client.get("/tarefas/")
    assert resposta.status_code == 401

def test_titulo_vazio(token_valido):
    resposta = client.post(
        "/tarefas/",
        json={"titulo": "", "descricao": "Descrição"},
        headers={"Authorization": f"Bearer {token_valido}"}
    )
    assert resposta.status_code == 422

def test_titulo_muito_longo(token_valido):
    titulo_longo = "a" * 101  # 101 caracteres, limite é 100
    resposta = client.post(
        "/tarefas/",
        json={"titulo": titulo_longo, "descricao": "Descrição"},
        headers={"Authorization": f"Bearer {token_valido}"}
    )
    assert resposta.status_code == 422

def test_deletar_tarefa_inexistente(token_valido):
    resposta = client.delete(
        "/tarefas/9999",
        headers={"Authorization": f"Bearer {token_valido}"}
    )
    assert resposta.status_code == 404
    assert resposta.json()["detail"] == "Tarefa não encontrada"
