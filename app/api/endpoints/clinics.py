from fastapi import APIRouter
from app.services.logic import listar_clinicas_ordenadas

router = APIRouter()

@router.get("/")
def listar_clinicas():
    return listar_clinicas_ordenadas()