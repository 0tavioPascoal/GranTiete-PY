capital=float(input("Digite o capital inicial: "))
taxa_de_juros=float(input("Digite a taxa de juros anual (em decimal): "))
tempo=float(input("Digite o tempo em investimento em anos: "))

montante= capital + (capital*taxa_de_juros*tempo)

print(" O montante após", tempo, "anos é de:", montante)