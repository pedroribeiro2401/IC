import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import pandas as pd

df = pd.read_csv('/home/pedro-ribeiro/.config/spyder-py3/y.csv')

desvios=df['y']

y_rms_teorico = 0.257419

plt.hist(desvios, bins=100, density=True, color='cyan', alpha=0.6, label='Simulação (Esferas Rígidas)',  range=(-0.8, 0.8))

x = np.linspace(-0.8, 0.8, 1000)
curva_teorica = norm.pdf(x, loc=0, scale=y_rms_teorico)

plt.plot(x, curva_teorica, 'r-', lw=2.5, label=f'Teoria (1 MeV): $\sigma$={y_rms_teorico:.4f} cm')

plt.title("Comparação: Simulação vs. Curva teórica", fontsize=17)
plt.xlabel("Desvio Lateral y (cm)",fontsize=17)
plt.ylabel("Densidade de Probabilidade",fontsize=16)
plt.legend( loc='upper left', fontsize="small")
plt.grid(alpha=0.3)
plt.show()