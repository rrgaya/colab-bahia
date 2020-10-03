from fastapi import FastAPI
from .routers import posts

app = FastAPI(
    title="Projeto de Colaboração Social",
    debug=True,
    description="Projeto de Colaboração Social por meio de fiscaliação."
)


@app.get("/", tags=["Colab"])
def index():
    return {"Project": "Colab"}


app.include_router(posts.router, prefix="/posts", tags=["Posts"])
