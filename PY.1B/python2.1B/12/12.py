n = int(input("Digite um número para calcular seu fatorial: "))

fatorial = 1
for i in range(1, n+1):
    fatorial *= 1

print(f"O número de {n} é {fatorial}.")