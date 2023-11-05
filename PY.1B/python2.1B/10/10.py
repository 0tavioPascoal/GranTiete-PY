numero= int(input("Digite um numero para ver sua tabuada:"))

for multiplicador in range(1,11):
    resultado = numero * multiplicador

    print(f"{numero} x {multiplicador} = {resultado}")