import pandas as pd

def load(df):
    """
    Salva o DataFrame transformado em um arquivo Parquet.

    Args:
        df (pandas.DataFrame): DataFrame a ser salvo.
    """
    df.to_parquet("data/output/vendas.parquet")