# rotas

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.services import user_service
from app.api.deps import get_db

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)