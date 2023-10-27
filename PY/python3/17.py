nota = float (input("Digite a nota do aluno: "))

if nota >= 9 and nota <= 10:
    categoria = "A"
elif nota >= 7 and nota < 9:
    categoria = "B"
elif nota >= 5 and nota < 7:
    categoria = "C"
elif nota >= 3 and nota < 5:
    categoria = "D"
else:
    categoria="F"
    print(f"A nota {nota} corresponde à categoria (categoria).")