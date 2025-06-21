from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    senha = Column(String)
    tasks = relationship("Task", back_populates="user")  # <-- tasks

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descricao = Column(String, nullable=True)
    concluida = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    criado_em = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    user = relationship("User", back_populates="tasks")  # <-- user
