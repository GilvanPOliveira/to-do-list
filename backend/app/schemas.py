from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    senha: str

class UserOut(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class TaskBase(BaseModel):
    titulo: str = Field(..., max_length=100)
    descricao: Optional[str] = None
    concluida: bool = False

class TaskCreate(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=100)
    descricao: Optional[str] = None
    concluida: bool = False

class TaskUpdate(TaskBase):
    pass

class TaskOut(BaseModel):
    id: int
    titulo: str
    descricao: str | None = None
    concluida: bool
    user_id: int
    criado_em: datetime

    model_config = ConfigDict(from_attributes=True)