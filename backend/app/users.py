from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .database import get_db
from .schemas import UserCreate
from .models import User
from .auth import hash_password
from pydantic import BaseModel

router = APIRouter()

class UsuarioResposta(BaseModel):
    mensagem: str

@router.post("/criar", response_model=UsuarioResposta, status_code=status.HTTP_201_CREATED)
def criar_usuario(usuario: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == usuario.email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="E-mail já cadastrado")
    
    novo_usuario = User(
        email=usuario.email,
        senha=hash_password(usuario.senha)
    )
    
    db.add(novo_usuario)
    db.commit()

    return {"mensagem": "Usuário criado com sucesso"}