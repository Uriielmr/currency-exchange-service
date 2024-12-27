from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.user_service import create_user, get_users
from app.database import get_db

router = APIRouter()

@router.post("/users/")
def add_user(name: str, email: str, daily_limit: float = 1000.0, db: Session = Depends(get_db)):
    """
        Create a new User
    """
    try:
        return create_user(db, name, email, daily_limit)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/users/")
def list_users(db: Session = Depends(get_db)):
    """
        Get all registered users
    """
    return get_users(db)
