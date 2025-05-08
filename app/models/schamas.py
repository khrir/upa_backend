from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Paciente(BaseModel):
    senha: int
    tipo_atendimento: str
    entrada: datetime
    saida: Optional[datetime]

class Fila(BaseModel):
    tamanho_fila: int
    tamanho_fila_pref: int
    espera: float
    espera_pref: float
    fila: List[Paciente]
