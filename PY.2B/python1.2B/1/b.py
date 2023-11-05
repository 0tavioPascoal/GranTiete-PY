import random

numparticipantes = list(range(1,200))

numeros = random.choices(numparticipantes, k = 5)

print(numeros)