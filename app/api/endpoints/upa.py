from fastapi import APIRouter
from app.services.fila_service import listar_fila_classificacao, listar_fila_atendimento_upa
from app.models.schemas import FilaClassificacao, FilaAtendimento

router = APIRouter()

@router.get("/{codigo_cnes}/filas", response_model=FilaClassificacao)
def obter_fila_classificacao(codigo_cnes: str):
    return listar_fila_classificacao(codigo_cnes)

@router.get("/{codigo_cnes}/picos")
def obter_picos_upa(codigo_cnes: str):
    return {"codigo_cnes": codigo_cnes, "picos": []}

@router.get("/{codigo_cnes}/leitos")
def obter_leitos_upa(codigo_cnes: str):
    return {"codigo_cnes": codigo_cnes, "leitos": []}

@router.get("/{codigo_cnes}/atendimento", response_model=FilaAtendimento)
def obter_fila_atendimento(codigo_cnes: str):
    return listar_fila_atendimento_upa(codigo_cnes)
