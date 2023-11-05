import pandas as pd

# Carregar  o dataset
data = pd.read_csv('billions.csv')

# Média do patrimônio líquido
media = data['finalWorth'].mean()
print(f'Média do patrimônio Líquido: ${media: .2f} bilhões')

# Mediana do patrimônio líquido
mediana = data['finalWorth'].median()
print(f'Media do patrimônio líquido: ${mediana: .2f} bilhões')

# Máximo patrimônio líquido
maximo = data['finalWorth'].max()
print(f'Máximo patrimônio líquido: ${maximo: .2f} bilhões')

# Minimo patrimônio líquido
minimo = data['finalWorth'].min()
print(f'Mínimo patrimônio líquido: ${minimo: .2f} bilhões')