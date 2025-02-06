import boto3
from io import StringIO

# Configuração do S3 (certifique-se de ter as credenciais da AWS configuradas)
s3_client = boto3.client('s3')

# Convertendo o DataFrame Polars para CSV (em formato de string)
csv_buffer = StringIO()
df_polars.write_csv(csv_buffer)
csv_buffer.seek(0)

# Nome do bucket e arquivo
bucket_name = 'meu-bucket-s3'
file_name = 'dados_transformados.csv'

# Carregando o CSV para o S3
s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=csv_buffer.getvalue())

print(f"Arquivo carregado com sucesso para o S3: s3://{bucket_name}/{file_name}")
