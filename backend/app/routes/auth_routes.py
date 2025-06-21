from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserLogin
from app.auth import criar_usuario, autenticar_usuario, criar_token_jwt

router = APIRouter()

@router.post("/register")
def registrar(usuario: UserCreate, db: Session = Depends(get_db)):
    usuario_existente = db.query(User).filter(User.email == usuario.email).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")
    novo_usuario = criar_usuario(db, usuario)
    access_token = criar_token_jwt(data={"sub": novo_usuario.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login")
def login(usuario: UserLogin, db: Session = Depends(get_db)):
    user = autenticar_usuario(db, usuario.email, usuario.senha)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = criar_token_jwt(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
