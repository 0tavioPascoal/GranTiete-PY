import random
numero_secreto = random. randint (1, 10)

print("Bem-vindo ao Jogo de Adivinhação!")
print ("Tente adivinhar o número secreto entre 1 e 10.")

while True:
    palpite = int(input("Digite seu palpite: "))
    if palpite == numero_secreto:
        print (f"Parabéns! Você acertou o número (numero-secreto).")
        break
    elif palpite < numero_secreto:
        print ("Tente um número maior.")
    else:
        print("Tente um número menor.")