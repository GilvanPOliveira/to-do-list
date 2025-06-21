from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_criar_usuario():
    resposta = client.post("/register", json={
        "email": "teste@example.com",
        "password": "senha123"
    })
    assert resposta.status_code == 200
    assert "access_token" in resposta.json()

def test_login_usuario():
    resposta = client.post("/login", json={
        "email": "teste@example.com",
        "senha": "senha123"
    })
    assert resposta.status_code == 200
    assert "access_token" in resposta.json()

def test_usuario_duplicado():
    email = "duplicado@example.com"
    senha = "senha123"
    resposta1 = client.post("/register", json={"email": email, "password": senha})
    assert resposta1.status_code == 200
    resposta2 = client.post("/register", json={"email": email, "password": senha})
    assert resposta2.status_code == 400
    assert resposta2.json()["detail"] == "E-mail já cadastrado"

def test_login_com_senha_errada():
    resposta = client.post("/login", json={
        "email": "teste@example.com",
        "senha": "senha_errada"
    })
    assert resposta.status_code == 401
    assert resposta.json()["detail"] == "Credenciais inválidas"

def test_acesso_com_token_invalido():
    resposta = client.get("/tarefas/", headers={"Authorization": "Bearer token_invalido"})
    assert resposta.status_code == 401
    assert resposta.json()["detail"] == "Token inválido ou expirado"
