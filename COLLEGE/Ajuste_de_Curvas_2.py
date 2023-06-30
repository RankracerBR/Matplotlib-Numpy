#Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Functions
def reta(x,a,b):
    return a * x + b

def expo(x,a,b):
    return a * np.exp(b*x)

#1
anos = np.array([1,2,3,4,5,6,7,8,9,10], dtype = float)
pop = np.array([50000, 52000, 54000, 56000, 59000, 62000, 65000, 68000, 72000, 76000], dtype = float)

coefs_1, _ = curve_fit(reta, anos,pop)

xi = np.linspace(1,10,100)
yi = reta(xi,*coefs_1)

print(reta(13,*coefs_1))

plt.scatter(anos,pop)
plt.plot(xi,yi)
plt.grid()
plt.show()

#2
tempo = np.array([0,10,30,60,90,120,140], dtype = float)
distancia = np.array([0,8,27,58,100,145,160], dtype = float)

coefs_2, _ = curve_fit(reta,tempo,distancia)

xii = np.linspace(0,140,100)
yii = reta(xii,*coefs_2)

print(reta(45,*coefs_2))
print(reta(180,*coefs_2))

plt.scatter(tempo,distancia)
plt.plot(xii,yii)
plt.grid()
plt.show()

#3
meses = np.array([1,2,3,4,5,6,7,8,9,10,11,12], dtype = float)
energia = np.array([200, 220, 230, 210, 240, 250, 270, 280, 300, 310, 320, 330], dtype = float)

coefs_3, _ = curve_fit(reta,meses,energia)
print(coefs_3)

xi = np.linspace(1,12,100)
yi = reta(xi,*coefs_3)

print(reta(13,*coefs_3))

plt.scatter(meses,energia)
plt.plot(xi,yi)
plt.grid()
plt.show()

#4
meses_2 = np.array([1,2,3,4,5,6], dtype = float)
cell = np.array([1200, 1300, 1400, 1600, 2000, 2500], dtype = float)

coefs_4, _ = curve_fit(expo, meses_2, cell)
print(coefs_4)

print(expo(7,*coefs_4))

xi = np.linspace(1,6,100)
yi = expo(xi,*coefs_4)

plt.scatter(meses_2,cell)
plt.plot(xi,yi)
plt.grid()
plt.show()

#5
meses_3 = np.array([1,2,3,4,5,6,7,8], dtype = float)
trafego = np.array([10, 15, 22, 33, 49, 73, 108, 160], dtype = float)

coefs_5, _ = curve_fit(expo,meses_3,trafego)
print(coefs_5)

print(expo(9,*coefs_5))

xi = np.linspace(1,8,100)
yi = expo(xi,*coefs_5)

plt.scatter(meses_3,trafego)
plt.plot(xi,yi)
plt.grid()
plt.show()

#6
horas = np.array([1,2,3,4,5,6,7,8], dtype = float)
rad = np.array([10, 8.1, 6.6, 5.4, 4.4, 3.6, 2.9, 2.4], dtype = float)

coefs_6, _ = curve_fit(expo,horas,rad)
print(coefs_6)

xi = np.linspace(1,8,100)
yi = expo(xi,*coefs_6)

plt.scatter(horas,rad)
plt.plot(xi,yi)
plt.grid()
plt.show()

print(expo(10,*coefs_6))

#7
anos = np.array([1,2,3,4,5,6,7,8,9,10], dtype = float) 
pib = np.array([1.2, 1.3, 1.5, 1.7, 2.0, 2.4, 2.9, 3.5, 4.2, 5.0], dtype = float)

coefs_7, _ = curve_fit(expo,anos,pib)
print(coefs_7)

xi = np.linspace(1,10,100)
yi = expo(xi,*coefs_7)

plt.scatter(anos,pib)
plt.plot(xi,yi)
plt.grid()
plt.show()

print(expo(11,*coefs_7))

#8
meses_4 = np.array([1,2,3,4,5,6,7,8,9,10,11,12], dtype = float)
usuarios = np.array([500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000, 512000, 1024000], dtype = float)

coefs_8, _ = curve_fit(expo,meses,usuarios)
print(coefs_8)

xi = np.linspace(1,12,100)
yi = expo(xi,*coefs_8)

plt.scatter(meses_4,usuarios)
plt.plot(xi,yi)
plt.grid()
plt.show()

print(expo(12,*coefs_8))

#9
distancia = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], dtype = float)
combustivel = np.array([12, 22, 31, 39, 48, 58, 66, 74, 84, 92], dtype = float)

coefs_9, _ =  curve_fit(expo,distancia,combustivel)
print(coefs_9)

xi = np.linspace(100,1000,100)
yi = expo(xi, *coefs_9)

plt.scatter(distancia, combustivel)
plt.plot(xi,yi)
plt.grid()
plt.show()

print(expo(750,*coefs_9))

print(expo(1200,*coefs_9))