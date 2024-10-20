# laennderaula04aovivo

Este projeto contém um conjunto de dados de vendas e scripts para análise.

## Instalação e Configuração

Siga estas etapas para configurar o projeto em sua máquina local:

1. Clone o repositório:
   ```
   git clone git@github.com:lvgalvao/laennderaula04aovivo.git
   ```

2. Navegue até o diretório do projeto:
   ```
   cd laennderaula04aovivo
   ```

3. Crie um ambiente virtual:
   ```
   python -m venv .venv
   ```

4. Ative o ambiente virtual:
   - No Windows:
     ```
     .venv\Scripts\activate
     ```
   - No macOS e Linux:
     ```
     source .venv/bin/activate
     ```

5. Instale as dependências do projeto (se houver um arquivo requirements.txt):
   ```
   pip install -r requirements.txt
   ```

## Uso

Para rodar o projeto, execute o comando:
```
python src/pipeline.py
```

## Estrutura do Projeto

- `data/input/vendas.csv`: Arquivo CSV contendo dados de vendas
- `data/output/vendas.parquet`: Arquivo Parquet contendo os dados transformados

## Contribuição

[Adicione instruções para contribuição, se aplicável]

## Licença

[Especifique a licença do projeto, se aplicável]
