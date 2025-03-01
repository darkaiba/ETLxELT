<h1>Porque Polars?</h1>
=======================

<h4>Desempenho</h4>
<p align="justify">Polars foi desenvolvido com o foco em desempenho e eficiência, utilizando processamento paralelo e operações vetorizadas.</p>
<p align="justify">Polars utiliza um modelo baseado em DataFrame Arrow (Apache Arrow), que oferece melhor desempenho devido a sua estrutura de dados otimizada para operações vetorizadas e em memória.</p>

<h4>Uso de Memória</h4>
<p align="justify">Polars é altamente eficiente em termos de uso de memória, utilizando menos memória para armazenar dados, especialmente ao trabalhar com grandes volumes de dados.</p>

<h4>API "Lazy"</h4>
<p align="justify">Polars suporta uma API Lazy, o que significa que você pode criar um pipeline de transformações sem realmente executar até que um resultado final seja solicitado.</p>
<p align="justify">O modo lazy no Polars permite que você crie um plano de execução e, em vez de calcular de imediato, o Polars vai otimizar a sequência de transformações e fazer os cálculos de forma mais eficiente.</p>

<h4>Paralelismo nativo</h4>
<p align="justify">Polars foi projetado desde o início para aproveitar o paralelismo e a executação distribuída, o que o torna muito mais eficiente para executar operações em múltiplos núcleos.</p>

<h4>API Consistente e Concisa</h4>
<p align="justify">Polars tem uma API mais consistente, especialmente se comparado à evolução do Pandas, que introduziu mudanças ao longo do tempo. A API do Polars é mais próxima de uma abordagem funcional.</p>

<h4>Facilidade com Tipos de Dados Complexos</h4>
<p align="justify">Polars possui suporte nativo para tipos de dados como Listas e Strings, tornando mais fácil lidar com tipos de dados mais complexos e hierárquicos.</p>

<h4>Compatibilidade com o Apache Arrow</h4>
<p align="justify">O Polars utiliza a Apache Arrow como seu formato de dados em memória. Isso facilita a integração com outras ferramentas que também utilizam o Arrow, como sistemas de armazenamento distribuído e Big Data.</p>

<h4>Integração com outras ferramentas</h4>
<p align="justify">O Polars tem uma integração mais simples e direta com PyArrow e outras tecnologias baseadas no Arrow.</p>

<h4>Conclusão</h4>
<p align="justify">Polars é ideal para quando você lida com grandes volumes de dados, precisa de alta performance, uso eficiente de memória, e deseja execução paralela.</p>

<h3>ETL com Polars</h3>
=======================
<p align="justify">O processo de ETL (Extract, Transform, Load) pode ser feito em 3 etapas: extrair os dados do CSV, transformá-los e depois carregá-los.</p>
<!--ts-->

    Etapa 1: Extrair os dados com Polars
    Primeiro, vamos ler o arquivo CSV usando a biblioteca Polars.
    
    Etapa 2: Transformar os dados
    Agora, vamos aplicar algumas transformações no dataframe.
    
    Etapa 3: Carregar os dados
    Agora, vamos carregar os dados para o DataWareHouse

<!--te-->

<h3>ELT com Polars</h3>
=======================
<p align="justify">O processo de ELT (Extract, Load, Transform) pode ser feito em 3 etapas: extrair os dados do CSV, carregá-los da origem e depois transformá-los.</p>
<!--ts-->

    Etapa 1: Extrair os dados com Polars
    Primeiro, vamos ler o arquivo CSV usando a biblioteca Polars.
    
    Etapa 2: Carregar os dados.
    Buscar os dados no DataLake
    
    Etapa 3: Transformar os dados
    Agora que temos os dados, o próximo passo é realizar o Transform.
    
    Etapa 4: Salvar os dados transformados para algum Data Warehouse
    Agora que os dados estão transformados, podemos fazer o Load novamente para algum Datawarehouse.

<!--te-->

<h3>Exemplo do Json de entrada</h3>
=======================
<!--ts-->

    {
        "input_file": None,
        "reading": {
            "reading_mode": 'csv',
            "host": None,
            "user": None,
            "password": None,
            "path": 'C:\\Documents\\datasets',
            "filename": 'dados.csv',
            "database": None,
            "type_database": None
        },
        "transformer": {
            "nulos_nan_zero": None,
            "remove_nan_nulos": None,
            "remove_doubles": None,
            "add_column_default":{
                "key": None,
                "value": None
            },
            "conversor_type":{
                "colum": None,
                "type": None
            },
            "remove_columns":['col1', 'col2'],
            "add_colums":{
                "name_colum": None,
                "operation": None
            },
        },
        "delivery":{
            "host": None,
            "user": None,
            "password": None,
            "database": None,
            "type_database": None,
            "table": None,
            "delivery_path": None,
            "bucket_s3": None
        },
        "default": None
    }

<!--te-->
