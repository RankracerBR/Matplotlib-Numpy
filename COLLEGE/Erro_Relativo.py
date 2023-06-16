import numpy as np
import matplotlib.pyplot as plt

parafuso_real = 10
parafuso_medido = 9

ponte_real = 10000
ponte_medida = 9999

erro_relativo = np.abs(parafuso_real - parafuso_medido) / np.abs(parafuso_real) * 100

erro_relativo_2 = np.abs(ponte_medida - ponte_real) / np.abs(ponte_real) * 100

print(f'O erro encontrado do parafuso: {erro_relativo}%')

print(f'O erro encontrado da ponte: {erro_relativo_2}%')