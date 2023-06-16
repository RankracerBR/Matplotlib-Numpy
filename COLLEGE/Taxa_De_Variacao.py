#Imports
import matplotlib.pyplot as plt
import numpy as np

#Funções
def derivada_discreta(x,y):
  v = []
  for i in range(len(x)):
    if i!=0 and i!=len(x)-1:
      d = (y[i+1] - y[i-1]) / (x[i+1] - x[i-1])
    elif i==0:
      d = (y[i+1] - y[i]) / (x[i+1] - x[i])
    elif i == len(x) - 1:
      d = (y[i] - y[i-1]) / (x[i] - x[i-1])
    v.append(d)
  return v

t = np.array([0.20,0.40,0.60,0.80,1.00,1.20,1.40,1.60,1.80,2.00,2.20,2.40,2.60,2.80,3.00])
a = np.array([0.50,0.80,0.60,0.20,0.40,0.50,0.60,0.80,0.90,0.70,0.60,0.40,0.20,0.30,0.40])

dxdy = derivada_discreta(t,a)
print(f'*Variações: {dxdy}')

plt.figure(figsize=(12,8))
plt.plot(t,dxdy, label="Tempo com variação")
plt.legend()
plt.grid()
plt.show()