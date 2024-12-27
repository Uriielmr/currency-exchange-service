from sqlalchemy.orm import Session
from app.models.user_model import User

def create_user(db: Session, name: str, email: str, daily_limit: float):
    
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise ValueError("This user already exists")
    
    new_user = User(name=name, email=email, daily_limit=daily_limit)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_users(db: Session):
    return db.query(User).all()
