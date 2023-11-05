jogos_recentes = ['League of Legends', 'Valorant', 'Rainbow Six', 'Apex Legends', 'Counter Strike 2']
print("Lista antiga: ", jogos_recentes)
jogos_recente = jogos_recentes.pop(2)
jogos_recentes.insert(0, jogos_recente)

jogos_recentes.pop(1)

print("Meus jogos atualizadas: ", jogos_recentes)