from fastapi import FastAPI
from app.generator import gerar_plano

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao Gerador de Planos de Aula!"}

@app.post("/gerar_plano")
def gerar(plano: dict):
    return gerar_plano(plano)
