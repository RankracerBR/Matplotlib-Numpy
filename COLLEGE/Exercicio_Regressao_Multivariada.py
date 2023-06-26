#Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Functions
def modelo_linear(x,a,b):
    return a*x + b

def modelo_multivariado(x,a,b,c):
    return a*x[0] + b*x[1] + c

def modelo_multivariado_2(x,a,b,c,d):
    return a*x[0] + b*x[1] + c*x[2] + d

dados = pd.read_csv('COLLEGE/casas.csv', sep=',')
print(dados)

print(dados['preco'])

plt.scatter(dados['area'],dados['preco'])
plt.grid()
plt.show()

coefs_area, _ = curve_fit(modelo_linear,dados['area'],dados['preco'])
print(coefs_area)

area = np.linspace(250,2200,100)
c_precos = modelo_linear(area,*coefs_area)

plt.scatter(dados['area'], dados['preco'])
plt.plot(area,c_precos,'r')
plt.grid()
plt.show()

coefs_area_2, _ = curve_fit(modelo_multivariado, [dados['area'], dados['preco']], dados['dist'])
print(coefs_area_2)

plt.scatter(dados['frente'],dados['dist'])
plt.grid()
plt.show()

coefs_area_preco_dist, _ = curve_fit(modelo_multivariado_2,[dados['area'],dados['acl_decl'],dados['dist']],dados['preco'])
print(coefs_area_preco_dist)

print(modelo_multivariado_2([359.87,0.75,200],*coefs_area_preco_dist))

dados.corr()

area = float(input('Informe a área: '))
acl_decl = float(input('Informe o sentindo predominante: '))
dist = float(input('Informe a distância: '))
print(modelo_multivariado_2([area,acl_decl,dist],*coefs_area_preco_dist))