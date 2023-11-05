import random

dado1 = list(range(1,6))

resultado1 = random.choices(dado1, k = 1)

dado2 = list(range(1,6))

resultado2 = random.choices(dado2, k = 1)

print(resultado1, resultado2)
