import boto3
from io import StringIO

# Convertendo o DataFrame Polars para CSV (em formato de string)
csv_buffer = StringIO()
df_athena.write_csv(csv_buffer)
csv_buffer.seek(0)

# Nome do arquivo no S3
new_file_name = 'dados_transformados.csv'

# Carregando o arquivo CSV para o S3 (Data Warehouse)
s3_client = boto3.client('s3')
s3_client.put_object(Bucket=bucket_name, Key=new_file_name, Body=csv_buffer.getvalue())

print(f"Arquivo transformado carregado com sucesso para o S3: s3://{bucket_name}/{new_file_name}")
