import numpy as np
import matplotlib.pyplot as plt

parafuso_real = 10
parafuso_medido = 9

erro_absoluto = np.abs(parafuso_real - parafuso_medido)
print(f'O erro encontrado do parafuso foi de {erro_absoluto} cm')

ponte_real = 10000
ponte_medida = 9999
erro_absoluto_2 = np.abs(ponte_real - ponte_medida)
print(f'O erro encontrado da ponte foi de {erro_absoluto_2}')