import pandas as pd
from pathlib import Path
from app.models.schemas import FilaClassificacao, FilaAtendimento, PacienteClassificacao, PacienteAtendimento

DATA_DIR = Path(__file__).parent.parent / "data"

def listar_fila_classificacao(codigo_cnes: str) -> FilaClassificacao:
    df = pd.read_csv(DATA_DIR / "fila_classificacao.csv")
    codigo_cnes = int(codigo_cnes)
    df_filtrada = df[df["codigo_cnes"] == codigo_cnes]

    pacientes = [
        PacienteClassificacao(
            senha=int(row["senha"]),
            tipo_atendimento=row["tipo_atendimento"],
            entrada=row["entrada"],
            saida=row["saida"]
        ) for _, row in df_filtrada.iterrows()
    ]
    
    return FilaClassificacao(
        tamanho_fila=len(df_filtrada),
        tamanho_fila_pref=df_filtrada[df_filtrada["tipo_atendimento"] == "preferencial"].shape[0],
        espera="00:15:00",
        espera_pref="00:10:00",
        fila=pacientes
    )

def listar_fila_atendimento_upa(codigo_cnes: str) -> FilaAtendimento:
    df = pd.read_csv(DATA_DIR / "fila_atendimento_upa.csv")
    codigo_cnes = int(codigo_cnes)
    df_filtrada = df[df["codigo_cnes"] == codigo_cnes]
    
    pacientes = [
        PacienteAtendimento(
            num_atendimento=int(row["num_atendimento"]),
            tipo_atendimento=row["tipo_atendimento"],
            entrada=row["entrada"],
            saida=row["saida"]
        ) for _, row in df_filtrada.iterrows()
    ]
    
    return FilaAtendimento(
        classificacao=df_filtrada["classificacao"].iloc[0] if not df_filtrada.empty else "nenhuma",
        tamanho_fila=len(df_filtrada),
        tamanho_fila_pref=df_filtrada[df_filtrada["tipo_atendimento"] == "preferencial"].shape[0],
        espera="00:30:00",
        espera_pref="00:20:00",
        fila=pacientes
    )
