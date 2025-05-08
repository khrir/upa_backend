from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from enum import Enum

class TipoAtendimento(str, Enum):
    normal = "normal"
    preferencial = "preferencial"

class ClassificacaoEnum(str, Enum):
    vermelho = "vermelho"
    amarelo = "amarelo"
    verde = "verde"
    azul = "azul"

class PacienteClassificacao(BaseModel):
    senha: int
    tipo_atendimento: TipoAtendimento
    entrada: datetime
    saida: Optional[datetime]

class PacienteAtendimento(BaseModel):
    num_atendimento: int
    tipo_atendimento: TipoAtendimento
    entrada: datetime
    saida: Optional[datetime]

class FilaClassificacao(BaseModel):
    tamanho_fila: int
    tamanho_fila_pref: int
    espera: str
    espera_pref: str
    fila: List[PacienteClassificacao]

class FilaAtendimento(BaseModel):
    classificacao: ClassificacaoEnum
    tamanho_fila: int
    tamanho_fila_pref: int
    espera: str
    espera_pref: str
    fila: List[PacienteAtendimento]

class EstabelecimentoOut(BaseModel):
    codigo_cnes: str
    codigo_tipo_unidade: int
    latitude: float
    longitude: float
    numero_telefone: str
    codigo_cep_estabelecimento: str
    endereco_estabelecimento: str
    numero_estabelecimento: str
    bairro_estabelecimento: str