import numpy as np
from scipy.interpolate import lagrange, interp1d
import matplotlib.pyplot as plt

#1
x = np.array([0,1,2,3,4,5], dtype = float) 
y = np.array([0,1,4,9,16,25], dtype = float)

spline = interp1d(x,y, kind='cubic')

poly_lagrange = lagrange(x,y)

x_novo = np.linspace(0,5,100)
y_novo = spline(x_novo)

plt.scatter(x,y, c='red')
plt.plot(x_novo,y_novo)
plt.plot(x_novo,poly_lagrange(x_novo))
plt.grid()
plt.show()

#2
altura = np.array([73,86,95,102,108,113,119,125,131,137,143,148], dtype = float)
peso = np.array([9.8,12.2,14.7,16.6,18.5,20.5,23.0,25.5,27.7,32.0,35.3,40], dtype = float)

estimativa_peso = lagrange(altura,peso)

x = np.linspace(73,148,100)
y = estimativa_peso(x)

plt.scatter(altura,peso, c="red")
plt.plot(x,y)
plt.grid()
plt.show()
print(estimativa_peso)
print('\n')

estimativa_1 = lagrange(altura[0:6], peso[0:6])
estimativa_2 = lagrange(altura[5:],peso[5:])

spline_peso = interp1d(altura,peso,kind='cubic')

x_novo = np.linspace(73,148)
x1 = np.linspace(73,113,100) 
x2 = np.linspace(113,148,100)
y1 = estimativa_1(x1)
y2 = estimativa_2(x2)
y_novo = spline_peso(x_novo)

plt.scatter(altura,peso,c='red')
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x_novo,y_novo)
plt.grid()
plt.show()

print(estimativa_1)
print('\n')
print(estimativa_2)

#3
x = np.linspace(0, 2*np.pi, 10)
y = np.sin(x) + 0.1 * np.random.randn(10)

x_1 = np.linspace(0,2*np.pi,100)
y_1 = np.sin(x_1)

plt.scatter(x,y,c='red')
plt.plot(x_1,y_1)
plt.grid()
plt.show()

lagrange_sinal = lagrange(x,y)

spline_sinal = interp1d(x,y,kind='cubic')

plt.scatter(x,y,c='red')
plt.plot(x_1,lagrange_sinal(x_1))
plt.plot(x_1,spline_sinal(x_1))
plt.grid()
plt.show()

#4
horas = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.], dtype=float)
temperatura = np.array([22, 20.5, 19, 18.5, 18, 18, 18.5, 19, 21, 23, 24, 24.5, 25, 26, 27, 28, 28, 26, 24.5, 23, 22, 22, 21.5, 21, 22], dtype=float)

spline_temp = interp1d(horas,temperatura,kind='cubic')

lagrange_temp = lagrange(horas,temperatura)

x_new = np.linspace(0,24,100)
y_new = spline_temp(x_new)

plt.scatter(horas,temperatura,c='red')
plt.plot(x_new,y_new)
plt.grid()
plt.show()

print(spline_temp(0.5))

horas = int(input('Informe a hora: '))
minutos = int(input('Informe os minutos: '))
horario = horas + minutos / 60
print(spline_temp(horario))
