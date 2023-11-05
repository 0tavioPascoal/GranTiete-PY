import pandas as pd

# Carregar o dataset
data = pd.read_csv('billions.csv')

# 1. Liste as top 5 categorias com o maior número de bilionários.
top_5_categorias = data['category'].value_counts().head(5)
print("Top 5 categorias com o maior número de bilionários:")
print(top_5_categorias)