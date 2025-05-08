from fastapi import APIRouter

router = APIRouter()

@router.get("/{codigo_cnes}/filas")
def obter_filas_ubs(codigo_cnes: str):
    return {"codigo_cnes": codigo_cnes, "filas": []}