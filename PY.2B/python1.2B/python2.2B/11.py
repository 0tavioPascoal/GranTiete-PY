import pandas as pd

# Carregar o dataset dos bilionários
df = pd.read_csv('billions.csv')

# Configurar o Pandas para exibir todas as linhas do DataFrame resultante
pd.set_option('display.max_rows', None)

# Convertendo a coluna que contém a data de nascimento dos bilionários para o formato de data
df['birthDate'] = pd.to_datetime(df['birthDate'])

# Filtrando o dataset para identificar os bilionários que têm seus aniversários em janeiro
january_billionaires = df[df['birthDate'].dt.month == 1]

# Exibindo uma lista dos bilionários que nasceram em janeiro, apresentando seus nomes e datas de nascimento
january_billionaires_info = january_billionaires[['name', 'birthDate']].reset_index(drop=True)
print(january_billionaires_info)
