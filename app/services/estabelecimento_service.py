import csv
from pathlib import Path
from app.models.schemas import EstabelecimentoOut

ARQUIVO_CSV = Path(__file__).parent.parent / "data" / "estabelecimentos.csv"

def listar_estabelecimentos() -> list[EstabelecimentoOut]:
    estabelecimentos = []
    with open(ARQUIVO_CSV, newline='', encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile)
        for linha in leitor:
            estabelecimentos.append(EstabelecimentoOut(
                codigo_cnes=linha['codigo_cnes'],
                codigo_tipo_unidade=int(linha['codigo_tipo_unidade']),
                latitude=float(linha['latitude']),
                longitude=float(linha['longitude']),
                numero_telefone=linha['numero_telefone'],
                codigo_cep_estabelecimento=linha['codigo_cep_estabelecimento'],
                endereco_estabelecimento=linha['endereco_estabelecimento'],
                numero_estabelecimento=linha['numero_estabelecimento'],
                bairro_estabelecimento=linha['bairro_estabelecimento'],
            ))
            
    return estabelecimentos