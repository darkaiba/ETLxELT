import boto3

# Configuração do S3 (certifique-se de ter as credenciais da AWS configuradas)
s3_client = boto3.client('s3')

# Caminho do arquivo local e do S3
file_path = 'dados_fakes.csv'
bucket_name = 'meu-bucket-s3'
file_name = 'dados_fakes.csv'

# Carregando o arquivo para o S3
with open(file_path, 'rb') as data:
    s3_client.upload_fileobj(data, bucket_name, file_name)

print(f"Arquivo carregado com sucesso para o S3: s3://{bucket_name}/{file_name}")