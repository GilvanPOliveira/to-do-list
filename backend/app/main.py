from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User, Task
from app.auth import autenticar_usuario, criar_token_jwt, obter_usuario_atual, hash_password
from app.schemas import UserCreate, TaskCreate, TaskOut, UserLogin
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth_routes, task_routes

app = FastAPI()

app.include_router(auth_routes.router)
app.include_router(task_routes.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/register")
def register(usuario: UserCreate, db: Session = Depends(get_db)):
    usuario_existente = db.query(User).filter(User.email == usuario.email).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")
    
    hashed_password = hash_password(usuario.password)
    novo_usuario = User(email=usuario.email, senha=hashed_password)
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    
    access_token = criar_token_jwt(data={"sub": novo_usuario.email})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/login")
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
