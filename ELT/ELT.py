import polars as pl
from datetime import datetime
from src.getdatas import DataReaderRemote, DataReaderFile
from ELT.Upload import LoadDatas
from ELT.Transformer import Transformer

class ELT:

     def __init__(self, json):
         self.json = json
         self.dados = None

     def extract(self):
         reader = None
         if self.json['input_file'] is False:
             # Busca dados em um servidor remoto ou banco de dados
             print("Buscando os dados")
             reader = DataReaderRemote(self.json)

             dados = []
             for chunk in reader.read_data():
                 dados.append(chunk)

             self.dados = pl.concat(dados)
         elif self.json['input_file'] is True:
             # Faz a leitura do arquivo de entrada (Local)
             print("Lendo o Arquivo de Entrada")
             reader = DataReaderFile(self.json)
             self.dados = reader.read_data()
         else:
             ValueError(f"Parametro não é válido, 'input_file' --> {self.json['input_file']}")

         print("Dados extraidos com Sucesso!")

     def transform(self):
         transformer = Transformer(self.json, self.dados)
         self.dados = transformer.run()

     def load(self):
         load = LoadDatas(self.json, self.dados)
         load.run()

     def run(self):
         self.extract()
         self.load()
         self.transform()
         self.load()