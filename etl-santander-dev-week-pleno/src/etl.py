"""
Pipeline ETL - Santander Dev Week
Autora: Barbara Ferreira

Descrição:
Pipeline ETL desenvolvido em Python para simular o processamento de dados
bancários em um cenário de indisponibilidade de API.
"""

import pandas as pd
from datetime import datetime


# =========================
# EXTRAÇÃO
# =========================
def extrair_dados(caminho: str) -> pd.DataFrame:
    """
    Realiza a leitura dos dados a partir de um arquivo CSV.

    :param caminho: Caminho do arquivo CSV
    :return: DataFrame com os dados brutos
    """
    return pd.read_csv(caminho)


# =========================
# TRANSFORMAÇÃO
# =========================
def classificar_cliente(saldo: float) -> str:
    """
    Classifica o cliente de acordo com o saldo disponível.
    """
    if saldo < 2000:
        return "Perfil Básico"
    elif saldo < 5000:
        return "Perfil Intermediário"
    return "Perfil Premium"


def gerar_mensagem(nome: str, saldo: float, perfil: str) -> str:
    """
    Gera uma mensagem personalizada para o cliente.
    """
    return (
        f"Olá, {nome}! 👋\n\n"
        f"Identificamos que você pertence ao {perfil}.\n"
        f"Seu saldo atual é R$ {saldo:,.2f}.\n\n"
        "Conte com nossos serviços para evoluir sua vida financeira 💙"
    )


def transformar_dados(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica regras de negócio e gera novas colunas.
    """
    df["perfil"] = df["saldo"].apply(classificar_cliente)

    df["mensagem"] = df.apply(
        lambda row: gerar_mensagem(
            row["nome"],
            row["saldo"],
            row["perfil"]
        ),
        axis=1
    )

    df["data_processamento"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return df


# =========================
# CARREGAMENTO
# =========================
def carregar_dados(df: pd.DataFrame, caminho_saida: str) -> None:
    """
    Salva os dados processados em um novo arquivo CSV.
    """
    df.to_csv(caminho_saida, index=False)


# =========================
# PIPELINE
# =========================
def main() -> None:
    caminho_entrada = "data/clientes.csv"
    caminho_saida = "data/mensagens_geradas.csv"

    df_bruto = extrair_dados(caminho_entrada)
    df_tratado = transformar_dados(df_bruto)
    carregar_dados(df_tratado, caminho_saida)

    print("✅ Pipeline ETL executado com sucesso!")


if __name__ == "__main__":
    main()
