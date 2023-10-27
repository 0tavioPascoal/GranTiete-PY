valor = int(input("Digite um valor para iniciar a contagem regressiva: "))

print(f"Contagem regressiva a partir  de {valor}: ")
for i in range(valor, -1, -1):
    print(i)