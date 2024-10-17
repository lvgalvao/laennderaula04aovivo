import pandas as pd

def transform(df):
    """
    Transforma os dados do DataFrame de vendas.

    Realiza as seguintes operações:
    1. Remove duplicatas
    2. Preenche valores nulos na coluna 'quantidade' com 0
    3. Cria uma coluna 'mes' baseada na coluna 'data'
    4. Cria/atualiza a coluna 'valor_total' multiplicando 'quantidade' por 'valor_unitario'

    Args:
        df (pandas.DataFrame): DataFrame de vendas a ser transformado.

    Returns:
        pandas.DataFrame: DataFrame transformado.
    """
    # Remoção de duplicatas
    df = df.drop_duplicates().copy()
    
    # Tratamento de nulls na coluna quantidade
    df['quantidade'] = df['quantidade'].fillna(0).copy()
    
    # Criação da coluna 'mes'
    df['mes'] = pd.to_datetime(df['data']).dt.month.copy()
    
    # Criação/atualização da coluna 'valor_total'
    df['valor_total'] = df['quantidade'] * df['valor_unitario'].copy()
    
    return df