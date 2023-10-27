numero = int(input("Digite um valor para verificar se ele é primo: "))
primo = True
if numero <= 1:
    primo = False
else:
    for divisor in range(2, numero):
        if numero % divisor == 0:
            primo = False
            break

if primo: 
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")