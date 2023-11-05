import pandas as pd

# Carregar o dataset
data = pd.read_csv('billions.csv')

# Quanto bilionários na lista são do gênero feminino? e do gênero masculino?
feminino_count=  data[data['gender'] == 'F'].shape[0]
masculino_count = data[data['gender'] == 'M'].shape[0]

print(f"Quantidade de bilionários femininos: {feminino_count}")
print(f"Quantidade de bilionários masculinos: {masculino_count}")

# 1. Selecionar os 10 países mais populosos
top_10_populous_countries = data.groupby('country')['population_country'].max().nlargest(10).index.tolist()

# 2. Contar bilionários para cada um dos 10 países
billionaire_counts = data[data['country'].isin(top_10_populous_countries)].groupby('country')['finalWorth'].sum()

# 3. Somar a fortuna dos bilionários para cada um dos 10 países 
total_worth_by_country = data[data['country'].isin(top_10_populous_countries)].groupby('country')['finalWorth'].sum()

# Exibir resultados 
print("Numero de bilionários por país:")
print(billionaire_counts)

print("\n Soma total da fortuna dos bilionários por país:")
print(total_worth_by_country)