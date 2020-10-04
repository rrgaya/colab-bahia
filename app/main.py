from fastapi import FastAPI
from .routers import posts
from .database import engine
from .models import Base


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Projeto de Colaboração Social",
    debug=True,
    description="Projeto de Colaboração Social por meio de fiscaliação."
)


@app.get("/", tags=["Colab"])
def index():
    return {"Project": "Colab"}


app.include_router(posts.router, prefix="/posts", tags=["Posts"])
