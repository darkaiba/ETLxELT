import polars as pl

class Transformer:
    def __init__(self, json, dados):
        """
        Construtor da classe Transformer.

        :param json: Dicionário com configurações para as transformações.
        :param dados: DataFrame do Polars a ser transformado.
        """
        self.json = json['transformer']
        self.dados = dados

    def run(self):
        """
        Método principal para execução das transformações.
        """
        # Substituir nulos e NaN por 0
        if self.json["nulos_nan_zero"]:
            self.substituir_nulos_e_nan_por_zero()


        # Remover valores NaN e nulos (se necessário)
        if self.json["remove_nan_nulos"]:
            self.remover_nan_nulos()

        # Remover dados duplicados
        if self.json["remove_doubles"]:
            self.remover_duplicados()

        # Adicionar coluna com valor padrão
        if "add_column_default" in self.json:
            self.adicionar_coluna_default(self.json["add_column_default"])

        # Converter tipos de colunas
        if "conversor_type" in self.json:
            self.converter_tipos(self.json["conversor_type"])

        # Remover colunas
        if "remove_columns" in self.json:
            self.remover_colunas(self.json["remove_columns"])

        # Adicionar novas colunas (média, mediana, desvio padrão, etc.)
        if "add_colums" in self.json:
            self.adicionar_colunas(self.json["add_colums"])

        return self.dados

    def substituir_nulos_e_nan_por_zero(self):
        """
        Substitui todos os valores nulos e NaN por 0 no DataFrame.
        """
        # Substituir nulos por 0
        self.dados = self.dados.fill_null(0)
        # Substituir NaN por 0
        self.dados = self.dados.fill_nan(0)

    def remover_nan_nulos(self):
        """
        Remove linhas com valores NaN ou nulos do DataFrame.
        """
        self.dados = self.dados.drop_nulls()

    def remover_duplicados(self):
        """
        Remove linhas duplicadas do DataFrame.
        """
        self.dados = self.dados.unique()

    def adicionar_coluna_default(self, config):
        """
        Adiciona uma nova coluna com um valor padrão ao DataFrame.

        :param config: Dicionário no formato {nome_coluna: valor_default}.
        """
        for nome_coluna, valor_default in config.items():
            if valor_default is None:
                # Adicionar coluna com valores null
                self.dados = self.dados.with_column(pl.lit(None).alias(nome_coluna))
            else:
                # Adicionar coluna com valor padrão especificado
                self.dados = self.dados.with_column(pl.lit(valor_default).alias(nome_coluna))

    def converter_tipos(self, conversoes):
        """
        Converte os tipos das colunas especificadas.

        :param conversoes: Dicionário no formato {coluna: tipo}.
        """
        for coluna, tipo in conversoes.items():
            if coluna in self.dados.columns:
                self.dados = self.dados.with_column(pl.col(coluna).cast(tipo))

    def remover_colunas(self, colunas):
        """
        Remove colunas especificadas do DataFrame.

        :param colunas: Lista de colunas a serem removidas.
        """
        self.dados = self.dados.drop(colunas)

    def adicionar_colunas(self, colunas):
        """
        Adiciona novas colunas ao DataFrame (média, mediana, desvio padrão, etc.).

        :param colunas: Dicionário no formato {nova_coluna: operacao}.
        """
        for nova_coluna, operacao in colunas.items():
            if operacao == "media":
                self.dados = self.dados.with_column(
                    pl.mean(pl.col(self.dados.columns)).alias(nova_coluna))
            elif operacao == "mediana":
                self.dados = self.dados.with_column(
                    pl.median(pl.col(self.dados.columns)).alias(nova_coluna))
            elif operacao == "desvio_padrao":
                self.dados = self.dados.with_column(
                    pl.std(pl.col(self.dados.columns)).alias(nova_coluna))
            elif operacao == "soma":
                self.dados = self.dados.with_column(
                    pl.sum(pl.col(self.dados.columns)).alias(nova_coluna))
            else:
                raise ValueError(f"Operação '{operacao}' não suportada.")