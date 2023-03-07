import matplotlib.pyplot as plt
import numpy as np

mes = np.array([1, 2, 3, 4, 5, 6, 7], dtype=float)
casos = np.array([9926, 76246, 681488, 2336640, 2835147, 4226655, 6942042], dtype=float)

plt.figure(figsize=(16,8))
plt.title('Casos de Covid-19')
plt.xlabel('# Meses')
plt.ylabel('# Casos')
plt.grid()
plt.scatter(mes,casos)
plt.ticklabel_format(axis='y', style='plain')#remove a notação ciêntifica(ie6)
plt.show()