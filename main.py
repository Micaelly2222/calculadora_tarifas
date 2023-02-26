from fastapi import FastAPI, Request
from fastapi import Query, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from models import DDDEnum, Tarifas
from tarifas import calcula_tarifas

app = FastAPI(title="Tarifa Q.uinino", description="Calculadora de tarifa Q.uinino")
templates = Jinja2Templates(directory="templates")


@app.get("/tarifas", response_model=Tarifas)
def calcula_tarifa(origem: DDDEnum = Query(..., description="DDD de Origem da ligação"),
                   destino: DDDEnum = Query(..., description="DDD de Destino da ligação"),
                   tempo: int = Query(..., description="Tempo **Total** da ligação")):
    """Função para calcular tarifas de diferentes planos"""
    if origem == destino:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="ligações de longa distância, os DDD devem ser diferentes")
    return calcula_tarifas(origem, destino, tempo)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Retorna a página inicial da aplicação"""
    return templates.TemplateResponse("index.html", {"request": request})
