# ponto de entrada

from fastapi import FastAPI
from app.api.v1.endpoints import user
from app.db.base import Base
from app.db.session import engine
from app.api.v1.endpoints import user

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Delivery API")

app.include_router(user.router, prefix="/api/v1/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "API Delivery rodando 🚀"}

# registrar rota no app

from app.api.v1.endpoints import auth

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])