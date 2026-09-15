import random
import matplotlib.pyplot as plt

mfp = 0.00152318 #em centímetros
dist_total = 10.0 #em centímetros
num_simulacoes = 10000

contagem_colisoes = []

for i in range(num_simulacoes):
    dist_percorrida = 0.0
    colisoes = 0

    while dist_percorrida < dist_total:
        passo = random.uniform(0,2*mfp)
        dist_percorrida += passo
        colisoes += 1
    
    contagem_colisoes.append(colisoes)

num_bins = 50
plt.figure(figsize=(10, 6))

contagens, limites_bins, patches = plt.hist(contagem_colisoes, bins=num_bins, color='#23eba5', edgecolor='black')

largura_bin = limites_bins[1] - limites_bins[0]

plt.title("Distribuição de colisões em 10cm (Modelo Uniforme)",fontsize=20)
plt.xlabel("Número de Colisões",fontsize=20)
plt.ylabel((f"Frequência (Contagens a cada {largura_bin:.0f} colisões)"),fontsize=17)
plt.show()