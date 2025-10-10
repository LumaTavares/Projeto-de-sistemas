from fastapi import FastAPI
from util.database import init_db
from controller.Pessoa import router as Pessoa_router
from controller.Endereco import router as End_router

app = FastAPI(title="FastAPI + SQLModel - MVC + Repository")

init_db()

app.include_router(Pessoa_router)
app.include_router(End_router)

@app.get("/")
def health():
    return {"status": "ok"}