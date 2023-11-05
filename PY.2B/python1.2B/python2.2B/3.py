import pandas as pd

# Carregar o data set
data = pd.read_csv('billions.csv')

# 1. Liste os 5 países com o maior número de bilionários.
top_5_paises = data['country'].value_counts().head(10)
print("Top 5 países com o maior número de bilionários:")
print(top_5_paises)

# 2. Quantos bilionários existem no Brasil?         
bilionários_brasil = data[data['country']== 'Brazil'].shape[0]
print(f" \n número de bilionários no Brasil: {bilionários_brasil}")