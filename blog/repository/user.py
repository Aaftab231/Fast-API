from .. import models, schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..hashing import Hash


def create(request: schemas.User, db: Session):
    new_user = models.User(username=request.username, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show_user(id: int, db: Session):
    users = db.query(models.User).filter(models.User.id == id).first()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} is not found.")
    return users

def show_all(db: Session):
    user = db.query(models.User).all()
    return user