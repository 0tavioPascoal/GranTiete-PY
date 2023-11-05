nota = float(input("Digite sua nota (0 a 10): "))

if nota >= 7:
    print("Você está aprovado!")
elif 5 <= nota < 7:
    print("Você está de recuperação!")
else:
    print("Reprovado!")