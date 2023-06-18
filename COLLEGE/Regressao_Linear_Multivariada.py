import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def modelo_linear(x,a,b):
    return a*x + b

def modelo_multivariado(x,a,b,c):
    return a*x[0] + b*x[1] + c

def modelo_multivariado_2(x,a,b,c,d):
    return a*x[0] + b*x[1] + c*x[2] + d

dados = pd.read_csv('COLLEGE/consumo_cerveja_limpo.csv',sep=';')
print(dados)
print('\n')

print(dados['temp_media'])
print('\n')

plt.scatter(dados['temp_media'], dados['consumo'])
plt.grid()
plt.show()

coef_temp,_ = curve_fit(modelo_linear,dados['temp_media'], dados['consumo'])
print(coef_temp)

temperaturas = np.linspace(10,30,100)
consumo_temp = modelo_linear(temperaturas,*coef_temp)

plt.scatter(dados['temp_media'], dados['consumo'])
plt.plot(temperaturas,consumo_temp,'r')
plt.grid()
plt.show()

modelo_linear(27,*coef_temp)

plt.scatter(dados['chuva'],dados['consumo'])
plt.grid()
plt.show()

coef_chuva,_ = curve_fit(modelo_linear,dados['chuva'],dados['consumo'])
print(coef_chuva)

temperaturas2 = np.linspace(0,90,100) 
consumo_temp2 = modelo_linear(temperaturas2,*coef_chuva)

plt.scatter(dados['chuva'], dados['consumo'])
plt.plot(temperaturas2,consumo_temp2,'r')
plt.grid()
plt.show()

print(modelo_linear(10,*coef_chuva))
print('\n')

coefs_temp_chuva, _ = curve_fit(modelo_multivariado,[dados['temp_media'],dados['chuva']],dados['consumo'])
print(coefs_temp_chuva)

print(modelo_multivariado([27,10],*coefs_temp_chuva))

plt.scatter(dados['fds'],dados['consumo'])
plt.grid()
plt.show()


coefs_temp_chuva_fds,_ = curve_fit(modelo_multivariado_2,[dados['temp_media'],dados['chuva'],dados['fds']],dados['consumo'])
print(coefs_temp_chuva_fds)

print(modelo_multivariado_2([27,10,1],*coefs_temp_chuva_fds))

#print(dados.corr())