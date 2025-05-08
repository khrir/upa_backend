from fastapi import APIRouter

router = APIRouter()

@router.get("/{codigo_cnes}/filas")
def obter_filas_upa(codigo_cnes: str):
    return {"codigo_cnes": codigo_cnes, "filas": []}

@router.get("/{codigo_cnes}/picos")
def obter_picos_upa(codigo_cnes: str):
    return {"codigo_cnes": codigo_cnes, "picos": []}

@router.get("/{codigo_cnes}/leitos")
def obter_leitos_upa(codigo_cnes: str):
    return {"codigo_cnes": codigo_cnes, "leitos": []}