import matplotlib.pyplot as plt
import numpy as np

mfp = 0.00152318 #em centímetros
col = 10000

dist =(np.random.exponential(scale=mfp, size=col)) 

num_bins = 50
plt.figure(figsize=(10, 6))

contagens, limites_bins, patches = plt.hist(dist * 1e6, range=(0,15000), bins=num_bins, color='#2bf0ec', edgecolor='black')

largura_bin = limites_bins[1] - limites_bins[0]

plt.ylabel(f"Frequência (Contagens a cada {largura_bin:.0f} nm)", fontsize=16)
plt.xlabel("Distância entre colisões (nm)", fontsize=18)
plt.title("Distribuição da Frequência do Livre Caminho Médio", fontsize=18)
plt.show()