numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

if numero1 <= numero2 and numero1 <= numero3:
    menor = numero1
elif numero2 <= numero1 and numero2 <= numero3:
    menor = numero2
else:
    menor = numero3

print(f"O menor número entre {numero3}, {numero1} e {numero2} é {menor}")