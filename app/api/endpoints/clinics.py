from fastapi import APIRouter
from app.services.estabelecimento_service import listar_estabelecimentos

router = APIRouter()

@router.get("/")
def listar_clinicas():
    return listar_estabelecimentos()