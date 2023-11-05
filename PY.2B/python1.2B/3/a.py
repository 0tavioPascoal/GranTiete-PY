
series_favoritas = ['Breaking Bad', 'Stranger things', 'The Witcher', 'Game of Thrones', 'Westworld']

series_favorita = series_favoritas.pop(2)
series_favoritas.insert(0, series_favorita)

series_favoritas.pop()

print("Minhas series atualizadas: ", series_favoritas)