quantidade= 15
preco_unitario= 10

if quantidade>20:
    desconto = 10
elif quantidade >10:
    desconto = 5
else:
    desconto = 0

    valor_desconto=(quantidade * preco_unitario * desconto)/100
    total_a_pagar=(quantidade * preco_unitario)- valor_desconto

    print(f"Total a pagar com desconto : R$ {total_a_pagar}")