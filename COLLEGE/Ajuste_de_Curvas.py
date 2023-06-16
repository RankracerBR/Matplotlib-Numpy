import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#1
def modelo_linear(x,a,b):
    return a*x+b

def modelo_polinomio_2(x,a,b,c):
    return a*x**2 + b*x + c

ano = np.array([1920,1930,1940,1950,1960,1970,1980,1990], dtype = float) 
pop = np.array([106.46,123.08,132.12,152.27,180.65,205.05,227.23,249.46], dtype = float)

coefs_linear, _ = curve_fit(modelo_linear,ano,pop)
print(coefs_linear)

coefs_poly, _ = curve_fit(modelo_polinomio_2,ano,pop)
print(coefs_poly)

y_linear =  modelo_linear(ano,*coefs_linear)
print(y_linear)

mse_linear = np.mean((pop - y_linear)**2)
print(mse_linear)

y_polinomio = modelo_polinomio_2(ano,*coefs_poly)
print(y_polinomio)

mse_polinomio = np.mean((pop - y_polinomio)**2)
print(mse_polinomio)
print('\n')

#2
horas = np.array([0, 4,8,12,16,20,24], dtype = float)
trafego = np.array([90,176,180,80,10,12,90], dtype = float)

coefs_traf_linear, _ = curve_fit(modelo_linear,horas,trafego)
print(coefs_traf_linear)

y_traf_linear = modelo_linear(horas,*coefs_traf_linear)
print(y_traf_linear)

mse_traf_linear = np.mean((trafego - y_traf_linear)**2)
print(mse_traf_linear)

coefs_traf_poli2, _ = curve_fit(modelo_polinomio_2,horas,trafego)
y_traf_poli2 = modelo_polinomio_2(horas,*coefs_traf_poli2)
mse_traf_poli2 = np.mean((trafego - y_traf_poli2)**2)
print(mse_traf_poli2)

x = np.linspace(0,24,100)
y_linear = modelo_linear(x,*coefs_traf_linear)
y_poli2 = modelo_polinomio_2(x,*coefs_traf_poli2)

plt.scatter(horas,trafego,c='red')
plt.plot(x,y_linear, label='Modelo Linear')
plt.plot(x,y_poli2,label='Modelo polinômio ordem 2')
plt.grid()
plt.show()

#3
def modelo_polinomio_3(x,a,b,c,d):
    return a*x**3 + b*x**2 + c*x+d

coefs_traf_n3, _ = curve_fit(modelo_polinomio_3,horas,trafego)
print(coefs_traf_n3)

y_n3 = modelo_polinomio_3(horas,*coefs_traf_n3)
print(y_n3)

mse_n3 = np.mean((trafego - y_n3)**2)
print(mse_n3)

x = np.linspace(0,24,100)
y_linear = modelo_linear(x,*coefs_traf_linear)
y_poli2 = modelo_polinomio_2(x,*coefs_traf_poli2)
y_poli3 = modelo_polinomio_3(x,*coefs_traf_n3)


plt.scatter(horas,trafego,c='red')
plt.plot(x,y_linear, label='Modelo Linear')
plt.plot(x,y_poli2,label='Modelo Polinômio ordem 2')
plt.plot(x,y_poli3,label='Modelo polinômio odem 3')
plt.grid()
plt.legend()
plt.show()

print(modelo_polinomio_3(14,*coefs_traf_n3))