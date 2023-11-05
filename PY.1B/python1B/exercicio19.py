preco_sem_taxa= 100
taxa_icms= 5.2

valor_icms= (preco_sem_taxa*taxa_icms)/100
preco_com_taxa= preco_sem_taxa +valor_icms

print(f" Preço do produto com ICMS: R$ {preco_com_taxa}")