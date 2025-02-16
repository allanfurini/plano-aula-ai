from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pdfkit
import json
import os
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader

app = FastAPI()

# Configuração do Jinja2 para templates
env = Environment(loader=FileSystemLoader("templates"))

# Verifica se o arquivo bncc.json existe para evitar erro de FileNotFoundError
BNCC_DATA = {}
if os.path.exists("bncc.json"):
    with open("bncc.json", "r", encoding="utf-8") as f:
        BNCC_DATA = json.load(f)
else:
    print("⚠️ Aviso: Arquivo bncc.json não encontrado. O sistema funcionará sem ele.")

# Modelo de entrada de dados
class PlanoAula(BaseModel):
    escola: str
    professor: str
    serie: str
    disciplina: str
    objetivos: str
    recursos: str
    metodologia: str
    atividades: str
    avaliacao: str
    competencias: list[str]
    data: str

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao Gerador de Planos de Aula!"}

@app.post("/gerar_plano")
def gerar_plano(plano: PlanoAula):
    try:
        # Carregar template HTML
        template = env.get_template("plano_aula_template.html")
        html_content = template.render(plano=plano)
        
        # Criar PDF
        pdf_path = "plano_aula.pdf"
        pdfkit.from_string(html_content, pdf_path)
        
        return {"message": "Plano de aula gerado com sucesso!", "pdf": pdf_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
