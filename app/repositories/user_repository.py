# acesso ao banco de dados para a entidade User

from sqlalchemy.orm import Session
from app.models.user import User

def create_user(db: Session, user):
    db_user = User(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# buscar usuario no banco

def get_user_by_email(db, email: str):
    return db.query(User).filter(User.email == email).first()