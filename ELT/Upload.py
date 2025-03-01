import boto3
from io import StringIO
from ELT import ModeDelivery
import paramiko as pk
from sqlalchemy import create_engine
import polars as pl
import pandas as pd

class LoadDatas:

    def __init__(self, json, dados):
        self.json = json['delivery']
        self.dados = dados

        self.local_path = None
        if self.json['input_file'] is True:
            self.local_path = json['input_file']
        else:
            self.local_path = json['default']

    def run(self):
        host = self.json['host']
        username = self.json['username']
        password = self.json['password']

        if self.json['delivery'] == ModeDelivery.DATABASE:
            database = self.json['database']
            type_database = self.json['type_database']

            if str(type_database).lower() == MYSQL:
                type_database = "mysql+pymysql"  # ou mysql
            elif str(type_database).lower() == ATHENA:
                type_database = "awsathena+rest"  # ou "awsathena"
            elif str(type_database).lower() == REDSHIFT:
                type_database = "redshift+psycopg2"  # ou "redshift"
            elif str(type_database).lower() == POSTGRES:
                type_database = "postgresql+psycopg2"  # ou "postgresql"
            elif str(type_database).lower() == SQLSERVER:
                type_database = "mssql+pyodbc"  # ou "mssql"
            else:
                raise ValueError(f"Tipo de banco de dados não reconhecido: {str(type_database).lower()}")

            print(f"Iniciando o acesso ao banco de dados: {host}/{database}")
            try:
                connection_string = f"{type_database}://{user}:{password}@{host}/{database}"
                engine = sqlalchemy.create_engine(connection_string)

                # Nome da tabela no banco de dados
                table_name = self.json['table']

                # Converter o DataFrame do Polars para Pandas
                df_polars = pl.DataFrame(self.dados)
                df_pandas = df_polars.to_pandas()

                # Salvar o DataFrame na tabela
                df_pandas.to_sql(table_name, con=engine, if_exists="replace", index=False)

                print(f"Dados salvos na tabela {table_name} com sucesso!")
            except Exception as e:
                raise ValueError(f"Nao foi possivel se conectar ao banco de dados. Erro: {e}")

        elif self.json['delivery'] == ModeDelivery.HOST:
            delivery_path = self.json['delivery_path']

            # Conecta ao servidor remoto via SSH
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            print(f"Iniciando conexão ao servidor remoto: {self.host}")

            try:
                ssh.connect(host=host, username=username, password=password)

                # Usa o SFTP para enviar o arquivo
                sftp = ssh.open_sftp()
                sftp.put(self.local_path, delivery_path)

                # Fecha a conexão SFTP e SSH
                sftp.close()
                ssh.close()

                print(f"Arquivo {self.local_path} enviado para {delivery_path} no servidor {hostname}.")
            except Exception as e:
                raise ValueError(f"Não foi possivel se conectar ao servidor. Erro: {e}")

        elif self.json['delivery'] == ModeDelivery.S3:
            # Configuração do S3 (certifique-se de ter as credenciais da AWS configuradas)
            s3_client = boto3.client('s3')

            df_polars = pl.DataFrame(self.dados)

            # Convertendo o DataFrame Polars para CSV (em formato de string)
            csv_buffer = StringIO()
            df_polars.write_csv(csv_buffer)
            csv_buffer.seek(0)

            # Nome do bucket e arquivo
            bucket_name = self.json['bucket_s3']
            file_name = self.local_path

            # Carregando o CSV para o S3
            s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=csv_buffer.getvalue())

            print(f"Arquivo carregado com sucesso para o S3: s3://{bucket_name}/{file_name}")
        else:
            ValueError(f"Parametro não é válido, 'delivery' --> {self.json['delivery']}")
