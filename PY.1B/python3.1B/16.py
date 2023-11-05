valor_total = float(input("Digite o valor total da compra: "))

if valor_total > 100:
    desconto = valor_total * 0.1
    valor_com_desconto = valor_total - desconto
    print (f"Você obteve um desconto de R$ {desconto:.2%}.")
else:
    valor_com_desconto = valor_total
    print (f"Valor a pagar: R$ {valor_com_desconto:.2£}")