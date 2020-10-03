from fastapi import FastAPI


app = FastAPI(
    title="Projeto de Colaboração Social",
    debug=True,
    description="Projeto de Colaboração Social por meio de fiscaliação."
)


@app.get("/")
def index():
    return {"Project": "Colab"}
