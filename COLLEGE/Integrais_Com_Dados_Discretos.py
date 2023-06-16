import numpy as np
import matplotlib.pyplot as plt

tempo =  np.array([1,2,3.25,4.5,6,7,8,9,9.5,10], dtype= float)
velocidade = np.array([5,6,5.5,7,8.5,8,6,7,7,5],dtype= float)

di = 0 
distancia = []

for i in range(len(tempo) - 1):
    di += (tempo[i+1] - tempo[i]) * (velocidade[i] + velocidade[i+1]) / 2
    distancia.append(di)
print(di)

plt.figure(figsize=(12,8))
plt.plot(tempo[:-1],distancia,'o-')
plt.grid()
plt.show()