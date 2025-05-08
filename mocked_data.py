import pandas as pd
from pathlib import Path

# Diretório de saída simulado
output_dir = Path("./app/data")
output_dir.mkdir(parents=True, exist_ok=True)

# Estabelecimentos mockados
estabelecimentos = pd.DataFrame([
    {
        "codigo_cnes": "1234567",
        "codigo_tipo_unidade": 1,
        "latitude": -9.6489,
        "longitude": -35.7089,
        "numero_telefone": "82999999999",
        "codigo_cep_estabelecimento": "57000000",
        "endereco_estabelecimento": "Rua das Clínicas",
        "numero_estabelecimento": "100",
        "bairro_estabelecimento": "Centro"
    },
    {
        "codigo_cnes": "7654321",
        "codigo_tipo_unidade": 2,
        "latitude": -9.6490,
        "longitude": -35.7090,
        "numero_telefone": "82988888888",
        "codigo_cep_estabelecimento": "57000001",
        "endereco_estabelecimento": "Avenida da Saúde",
        "numero_estabelecimento": "200",
        "bairro_estabelecimento": "Jatiúca"
    }
])

# Fila de classificação (UPA)
fila_classificacao = pd.DataFrame([
    {
        "codigo_cnes": "1234567",
        "senha": 101,
        "tipo_atendimento": "preferencial",
        "entrada": "2025-05-08T08:00:00",
        "saida": "2025-05-08T08:15:00"
    },
    {
        "codigo_cnes": "1234567",
        "senha": 102,
        "tipo_atendimento": "normal",
        "entrada": "2025-05-08T08:05:00",
        "saida": "2025-05-08T08:20:00"
    }
])

# Fila de atendimento (UPA)
fila_atendimento_upa = pd.DataFrame([
    {
        "codigo_cnes": "1234567",
        "classificacao": "vermelho",
        "num_atendimento": 1001,
        "tipo_atendimento": "preferencial",
        "entrada": "2025-05-08T08:20:00",
        "saida": "2025-05-08T08:45:00"
    },
    {
        "codigo_cnes": "1234567",
        "classificacao": "verde",
        "num_atendimento": 1002,
        "tipo_atendimento": "normal",
        "entrada": "2025-05-08T08:25:00",
        "saida": "2025-05-08T08:50:00"
    }
])

# Fila de atendimento (UBS)
fila_atendimento_ubs = pd.DataFrame([
    {
        "codigo_cnes": "7654321",
        "num_atendimento": 2001,
        "tipo_atendimento": "normal",
        "entrada": "2025-05-08T09:00:00",
        "saida": "2025-05-08T09:25:00"
    },
    {
        "codigo_cnes": "7654321",
        "num_atendimento": 2002,
        "tipo_atendimento": "preferencial",
        "entrada": "2025-05-08T09:05:00",
        "saida": "2025-05-08T09:30:00"
    }
])

# Salvando arquivos CSV
estabelecimentos.to_csv(output_dir / "estabelecimentos.csv", index=False)
fila_classificacao.to_csv(output_dir / "fila_classificacao.csv", index=False)
fila_atendimento_upa.to_csv(output_dir / "fila_atendimento_upa.csv", index=False)
fila_atendimento_ubs.to_csv(output_dir / "fila_atendimento_ubs.csv", index=False)

import ace_tools as tools; tools.display_dataframe_to_user(name="Estabelecimentos e Filas CSV", dataframe=estabelecimentos)
