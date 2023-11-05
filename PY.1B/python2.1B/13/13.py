termo1, termo2 = 0, 1
print("Os primeiros 10 termos da sequência de fibonacci")

for i in range(10):
    print(termo1)
    proximo_termo = termo1 + termo2
    termo1, termo2 = termo2, proximo_termo