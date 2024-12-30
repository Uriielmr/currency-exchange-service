from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager
from app.models.base import Base
from app.application import create_app

DATABASE_URL = "sqlite:///./exchange_API.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear las tablas de la db
Base.metadata.create_all(bind=engine)

# para la conexion de la db 
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application startup")  # inicia app
    yield
    print("Application shutdown")  # termina app

# crea aplicacion
app = create_app()
app.router.lifespan_context = lifespan

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


