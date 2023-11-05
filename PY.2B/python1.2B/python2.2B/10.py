import pandas as pd

# Carregar o dataset dos bilionários
df = pd.read_csv('billions.xlsx')

# Configurar o Pandas para exibir todas as linhas do DataFrame resultante
pd.set_option('display.max_rows', None)

# Filtrar o dataset para selecionar os bilionários relacionados à indústria tecnológica
tech_billionaires = df[df['industry'] == 'Technology']

# Apresentar uma lista dos bilionários de tecnologia com seus nomes, países de origem e valor total de riqueza
tech_billionaires_info = tech_billionaires[['name', 'country', 'netWorth']].reset_index(drop=True)
print(tech_billionaires_info)

