import os
from typing import List
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="API do Alekeee")

class Item(BaseModel):
    nome: str
    preco: float
    quantidade: int

class ItemProcessado(BaseModel):
    nome: str
    preco_total: float
    mensagem: str


@app.get("/", response_class=HTMLResponse)
def home():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>API - Home</title>
    </head>
    <body>
        <h1>API do Alekeee
    </h1>
        <p>Rotas:</p>
        <ul>
            <li><a href="/docs">Documentacao (/docs)</a></li>
            <li><a href="/health">Healthcheck (/health)</a></li>
            <li><a href="/config/envs">Variaveis de Ambiente (/config/envs)</a></li>
        </ul>
    </body>
    </html>
    """
    return html


@app.get("/health")
def health():
    return {"status": "ok"}



@app.get("/config/envs")
def envs():
    return {
        "app_name": os.getenv("APP_NAME"),
        "app_version": os.getenv("APP_VERSION"),
        "environment": os.getenv("ENVIRONMENT")
    }


@app.post("/items", response_model=List[ItemProcessado])
def criar_itens(itens: List[Item]):
    resultado = []
    for item in itens:
        total = item.preco * item.quantidade
        resultado.append({
            "nome": item.nome,
            "preco_total": total,
            "mensagem": f"Item {item.nome} Cadastrado!"
        })
    return resultado
