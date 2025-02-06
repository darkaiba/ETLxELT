import polars as pl
from datetime import datetime

# Carregar o arquivo CSV usando Polars
df_polars = pl.read_csv('dados_fakes.csv')

# Exibindo as primeiras linhas do DataFrame
print(df_polars.head())

# Transformando os dados (por exemplo, calculando a idade das pessoas)
df_polars = df_polars.with_columns(
    pl.col("Data_Nascimento")
    .str.strptime(pl.Date, fmt="%Y-%m-%d")
    .alias("Data_Nascimento")
)

# Calculando a idade (assumindo que a data de hoje é 2025-02-06)
hoje = datetime.today()
df_polars = df_polars.with_columns(
    (hoje.year - pl.col("Data_Nascimento").dt.year()).alias("Idade")
)

# Exibindo o DataFrame transformado
print(df_polars.head())