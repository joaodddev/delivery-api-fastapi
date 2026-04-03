# regras de negócio

from sqlalchemy.orm import Session
from app.repositories import user_repository
from app.core.security import hash_password

def create_user(db: Session, user):
    user.password = hash_password(user.password)
    return user_repository.create_user(db, user)