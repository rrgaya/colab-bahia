from fastapi import APIRouter
from ..database import SessionLocal

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.get("/")
def post():
    """Endpoint de visualização de posts de fiscalização social
    """
    return {"data": "Posts"}


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
