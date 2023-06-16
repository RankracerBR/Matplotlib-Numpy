import matplotlib.pyplot as plt
import numpy as np

def polinomio(x):
    return 2*x**2+3*x+2

x = np.linspace(0,100,100)
y = polinomio(x)

plt.figure()
plt.grid()
plt.title('Polinômio')
plt.plot(x,y)
plt.scatter(x,y)
plt.show()
 