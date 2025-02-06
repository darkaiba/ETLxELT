from pyathena import connect
import polars as pl
from datetime import datetime

# Conectar ao Athena
conn = connect(region_name='us-east-1', s3_staging_dir='s3://meu-bucket-s3/athena-results/')

# Consultar os dados no Athena
query = "SELECT * FROM dados_fakes"
df_athena = pl.from_pandas(pd.read_sql(query, conn))

# Verificando os dados carregados
print(df_athena.head())

# Transformando a coluna 'Data_Nascimento' para formato de data
df_athena = df_athena.with_columns(
    pl.col("Data_Nascimento").str.strptime(pl.Date, fmt="%Y-%m-%d").alias("Data_Nascimento")
)

# Calculando a idade das pessoas (assumindo que a data de hoje é 2025-02-06)
hoje = datetime.today()
df_athena = df_athena.with_columns(
    (hoje.year - pl.col("Data_Nascimento").dt.year()).alias("Idade")
)

# Exibindo os dados transformados
print(df_athena.head())