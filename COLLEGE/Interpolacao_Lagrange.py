import numpy as np
import matplotlib.pyplot  as plt
from scipy.interpolate import lagrange

#1
x = np.array([0,1,2], dtype = float)
y = np.array([1,3,2], dtype = float)

plt.scatter(x,y)
plt.grid()
plt.show()

polinomio = lagrange(x,y)
print(polinomio)

def f(x):
    return -1.5*x**2 + 3.5*x + 1

x_new = np.linspace(0,2,100)
y_new = f(x_new)
plt.plot(x_new,y_new)
plt.scatter(x,y,c='red')
plt.grid()
plt.show()

#2
dias = np.array([1,3,5,7,9], dtype = float)
alturas = np.array([0,2,7,13,19], dtype = float)

plt.scatter(dias,alturas)
plt.grid()
plt.show()

polinomio = lagrange(dias,alturas)
print(polinomio)

x_dias = np.linspace(1,9,100)
y_alturas = polinomio(x_dias)

plt.scatter(dias, alturas, c='red')
plt.plot(x_dias,y_alturas)
plt.grid()
plt.show()

#3
horas = np.array([0,6,12,18,24], dtype = float)
temperaturas = np.array([10,12,20,16,10], dtype = float)
polinomio2 = lagrange(horas,temperaturas)
print(polinomio2)

x_horas = np.linspace(0,24,100)
plt.scatter(horas,temperaturas,c='red')
plt.plot(x_horas,polinomio2(x_horas))
plt.grid()
plt.show()