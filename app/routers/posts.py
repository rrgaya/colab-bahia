from typing import Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from app import crud


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.get("/")
def get_all_post(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    """Endpoint de visualização de posts de fiscalização social
    """
    posts = crud.get_posts(db, skip=skip, limit=limit)
    if posts == []:
        return {"Message": "Post not found"}
    return {"data": posts}


@router.post("/")
def create_post():
    """Endpoint de visualização de posts de fiscalização social
    """
    return {"data": "Posts"}


@router.patch("/")
def patch_post():
    """Endpoint de visualização de posts de fiscalização social
    """
    return {"data": "Posts"}
