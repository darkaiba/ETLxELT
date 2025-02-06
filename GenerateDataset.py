import pandas as pd
import random
import string

# Função para gerar um nome aleatório
def gerar_nome():
    return ''.join(random.choices(string.ascii_uppercase, k=5))

# Função para gerar um sobrenome aleatório
def gerar_sobrenome():
    return ''.join(random.choices(string.ascii_uppercase, k=7))

# Função para gerar uma data de nascimento aleatória
def gerar_data_nascimento():
    ano = random.randint(1970, 2000)
    mes = random.randint(1, 12)
    dia = random.randint(1, 28)  # Para garantir que o dia não ultrapasse o limite do mês
    return f'{ano}-{mes:02d}-{dia:02d}'

# Função para gerar um valor de salário aleatório
def gerar_salario():
    return round(random.uniform(3000, 10000), 2)

# Gerando uma base de dados fictícia
dados = []
for _ in range(100):
    nome = gerar_nome()
    sobrenome = gerar_sobrenome()
    data_nascimento = gerar_data_nascimento()
    salario = gerar_salario()
    dados.append([nome, sobrenome, data_nascimento, salario])

# Criando um DataFrame com o Pandas
df = pd.DataFrame(dados, columns=["Nome", "Sobrenome", "Data_Nascimento", "Salario"])

# Salvando em um arquivo CSV
df.to_csv('dados_fakes.csv', index=False)