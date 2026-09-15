import numpy as np
import pandas as pd

mfp        = 0.0000366   
dist_total = 10.0  
theta_0_col = 0.00008529  
num_simulacoes = 10000
lote   = 100                    
n_passos = int(dist_total / mfp) + 500  

print(f"Colisões por trajetória : {int(dist_total/mfp):,}")
print(f"Lotes de {lote} → {num_simulacoes//lote} iterações")
print(f"Iniciando simulação...\n")

y_total = []

for i in range(0, num_simulacoes, lote):
    passos = np.random.exponential(scale=mfp, size=(lote, n_passos))
    thetas = np.random.normal(0, theta_0_col, size=(lote, n_passos))
    thetas = np.clip(thetas, -np.pi/2, np.pi/2)

    dist_acum = np.cumsum(passos, axis=1)
    dentro    = dist_acum <= dist_total

    angulos_acum  = np.cumsum(thetas * dentro, axis=1)

    angulos_antes         = np.roll(angulos_acum, 1, axis=1)
    angulos_antes[:, 0]   = 0.0

    y_lote = np.sum(passos * np.sin(angulos_antes) * dentro, axis=1)
    y_total.extend(y_lote)

    if (i // lote + 1) % 20 == 0:
        print(f"  {i + lote}/{num_simulacoes} simulações concluídas...")

y_total = np.array(y_total)
pd.DataFrame({'y': y_total}).to_csv('y.csv', index=False)

print(f"\n=== RESULTADOS ===")
print(f"Simulações : {num_simulacoes}")
print(f"Média      : {np.mean(y_total):.5f} cm")
print(f"σ          : {np.std(y_total):.5f} cm")
print(f"Lynch-Dahl : 0.25740 cm")
print(f"Salvo em   : y.csv")