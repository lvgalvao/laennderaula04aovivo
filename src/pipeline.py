from extract_etl import extract
from transform_etl import transform
from load_etl import load
    
def pipeline(path: str):
    """
    Executa o pipeline completo de ETL (Extract, Transform, Load).

    Args:
        path (str): Caminho para o arquivo CSV de entrada.
    """
    df = extract(path)
    df = transform(df)
    load(df)

pipeline("data/input/vendas.csv")
