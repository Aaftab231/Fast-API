from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def get_blog(id: int, db: Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found.")
    return blogs

def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title = request.title, body = request.body, user_id = 2)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} does not exist.")
    blog.update(request.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return {"msg": f"Blog with id {id} updated successfully"}

def delete(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} does not exist.")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"msg": "Blog deleted successfully"}

