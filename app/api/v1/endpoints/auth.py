# rota - login

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.services.auth_service import authenticate_user
from app.schemas.auth import Token

router = APIRouter()

@router.post("/login", response_model=Token)
def login(email: str, password: str, db: Session = Depends(get_db)):
    token = authenticate_user(db, email, password)

    if not token:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    return {
        "access_token": token,
        "token_type": "bearer"
    }