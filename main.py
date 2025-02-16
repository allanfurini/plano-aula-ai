from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pdfkit
import json
import os
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

app = FastAPI()

# Configuração do Jinja2 para templates
env = Environment(loader=FileSystemLoader("templates"))

# Servir arquivos estáticos (CSS e JS)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# Verifica se o arquivo bncc.json existe
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

# 🟢 Rota principal para exibir a interface do Gerador de Planos de Aula
@app.get("/", response_class=HTMLResponse)
def serve_index():
    index_path = Path("frontend/index.html")
    if index_path.exists():
        return index_path.read_text(encoding="utf-8")
    raise HTTPException(status_code=404, detail="Página não encontrada")

# 🟢 Rota para gerar o plano de aula em PDF
@app.post("/gerar_plano")
def gerar_plano(plano: PlanoAula):
    try:
        # Carregar template HTML
        template = env.get_template("plano_aula_template.html")
        html_content = template.render(plano=plano)

        # Criar PDF
        pdf_path = "plano_aula.pdf"
        pdfkit.from_string(html_content, pdf_path)

        return FileResponse(pdf_path, media_type="application/pdf", filename="plano_aula.pdf")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
