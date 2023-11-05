
livros_favoritos = ['Harry Potter', 'Percy Jackson', 'The Witcher', 'Game of Thrones', 'Pequeno Príncipe']

print("Lista antiga: ", livros_favoritos)

livros_favorito = livros_favoritos.pop(3)
livros_favoritos.insert(0, livros_favorito)

livros_favoritos.pop(2)

print("Minhas series atualizadas: ", livros_favoritos)