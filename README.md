# upa_backend


## Onde conseguir os dados dos estabelecimentos
https://apidadosabertos.saude.gov.br/v1/#/CNES
https://apidadosabertos.saude.gov.br/v1/#/Assist%C3%AAncia%20%C3%A0%20Sa%C3%BAde

## Estrutura de Modelos
Estabelecimento
- codigo_cnes 
- codigo_tipo_unidade
- Latitude
- Longitude
- numero_telefrone
- codigo_cep_estabelecimento
- endereco_estabelecimento
- numero_estabelecimento
- bairro_estabelecimento

UPA
- Fila de classificacao
    - tamanho_fila
    - tamanho_fila_pref
    - espera 
    - espera_pref
    - fila[lista]
        - paciente
            - senha(int)
            - tipo_atendimento(preferencial ou normal)
            - entrada(timestamp)
            - saida(timestamp) 

- Filas de atendimento
    - classificacao(enum)
    - tamanho_fila(int)
    - tamanho_fila_pref(int)
    - espera(duration)
    - espera_pref(duration)
    - fila[lista]
        - paciente
            - num_atendimento(int)
            - tipo_atendimento(preferencial ou normal)
            - entrada(timestamp)
            - saida(timestamp) 

UBS
- Fila de atendimento
    - tamanho_fila(int)
    - tamanho_fila_pref(int)
    - espera(duration)
    - espera_pref(duration)
    - fila[lista]
        - paciente
            - num_atendimento(int)
            - tipo_atendimento(preferencial ou normal)
            - entrada(timestamp)
            - saida(timestamp) 

- Picos[WIP]
- Leitos[WIP]

## Endpoints
### Endpoints de usuario
    - GET /clinics/
        - Obtem as UPAs e UBSs ordenadas por distancia

    - GET /clinics/{codigo_cnes}
        - Obtem estabelecimento utilizando cnes

    - GET /clinics/upa/{codigo_cnes}/filas 
        - Obtem as filas da upa atraves do cnes

    - GET /clinics/upa/{codigo_cnes}/picos
        - Obtem os horarios de pico da UPA atraves do cnes da clinica

    - GET /clinics/upa/{codigo_cnes}/leitos
        - Obtem os leitos disponiveis na UPA

    - GET /clinics/upa/
        - Obtem as UPAs ordenadas por distancia

    - GET /clinics/ubs/
        - Obtem as UBSs ordenadas por distancia

    - GET /clinics/ubs/{codigo_cnes}/filas 
        - Obtem as filas da ubs atraves do cnes

### Endpoints de prestador de servico
    - GET /clinics/
