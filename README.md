Porque Polars?

Desempenho
Polars foi desenvolvido com o foco em desempenho e eficiência, utilizando processamento paralelo e operações vetorizadas.
Polars utiliza um modelo baseado em DataFrame Arrow (Apache Arrow), que oferece melhor desempenho devido a sua estrutura de dados otimizada para operações vetorizadas e em memória.

Uso de Memória
Polars é altamente eficiente em termos de uso de memória, utilizando menos memória para armazenar dados, especialmente ao trabalhar com grandes volumes de dados.

API "Lazy"
Polars suporta uma API Lazy, o que significa que você pode criar um pipeline de transformações sem realmente executar até que um resultado final seja solicitado.
O modo lazy no Polars permite que você crie um plano de execução e, em vez de calcular de imediato, o Polars vai otimizar a sequência de transformações e fazer os cálculos de forma mais eficiente.

 Paralelismo nativo
Polars foi projetado desde o início para aproveitar o paralelismo e a executação distribuída, o que o torna muito mais eficiente para executar operações em múltiplos núcleos.

API Consistente e Concisa
Polars tem uma API mais consistente, especialmente se comparado à evolução do Pandas, que introduziu mudanças ao longo do tempo. A API do Polars é mais próxima de uma abordagem funcional.

Facilidade com Tipos de Dados Complexos
Polars possui suporte nativo para tipos de dados como Listas e Strings, tornando mais fácil lidar com tipos de dados mais complexos e hierárquicos.

Compatibilidade com o Apache Arrow
O Polars utiliza a Apache Arrow como seu formato de dados em memória. Isso facilita a integração com outras ferramentas que também utilizam o Arrow, como sistemas de armazenamento distribuído e Big Data.

Integração com outras ferramentas
O Polars tem uma integração mais simples e direta com PyArrow e outras tecnologias baseadas no Arrow.

Conclusão:
Polars é ideal para quando você lida com grandes volumes de dados, precisa de alta performance, uso eficiente de memória, e deseja execução paralela.

========================================================================================================================================================
ETL com Polars
O processo de ETL (Extract, Transform, Load) pode ser feito em 3 etapas: extrair os dados do CSV, transformá-los e depois carregá-los para o AWS.

Etapa 1: Extrair os dados com Polars
Primeiro, vamos ler o arquivo CSV usando a biblioteca Polars.

Etapa 2: Transformar os dados
Agora, vamos aplicar algumas transformações no dataframe.

Etapa 3: Carregar os dados para o AWS (S3)
Agora, vamos carregar os dados para o Amazon S3, usando o boto3, que é a biblioteca oficial da AWS para interagir com seus serviços.

Resumo do Processo:
Criamos uma base de dados fictícia em CSV.
Usamos Polars para realizar transformações no dataframe, como calcular a idade a partir da data de nascimento.
Carregamos os dados transformados para o AWS S3.

========================================================================================================================================================
ELT com Polars
Etapa 1: Carregar os dados no AWS Athena.

Etapa 2: Transformar os dados com Polars
Agora que temos os dados no Athena, o próximo passo é realizar o Transform usando o Polars. Vamos conectar ao Athena e ler os dados usando boto3 e PyAthena.

Etapa 3: Carregar os dados transformados para o S3 (Data Warehouse)
Agora que os dados estão transformados, podemos fazer o Load novamente para o S3 como um novo arquivo CSV, que será usado como um data warehouse.