CREATE EXTERNAL TABLE IF NOT EXISTS dados_fakes (
    Nome STRING,
    Sobrenome STRING,
    Data_Nascimento STRING,
    Salario DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 's3://meu-bucket-s3/dados_fakes.csv';