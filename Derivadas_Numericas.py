import matplotlib.pyplot as plt 
import numpy as np 

#Derivada Progressiva

def f(x):
    return x**2

def f2(x):
    return x**3

def derivada_progressiva(funcao,h,x):
    return (funcao(x+h) - funcao(x)) / h

h = 0.0001
x = 2
dfdx = derivada_progressiva(f,h,x)
print(f'{dfdx:.3f}')
print('\n')

h_2 = 0.1
x_2 = 2
dfdx_2 = derivada_progressiva(f2,h,x)
print(f'{dfdx_2:.3f}')
print('\n')

valor_real = 12
erro_relativo = np.abs(valor_real - dfdx_2) / np.abs(valor_real)*100
print(f'{erro_relativo}')
print('\n')
#Derivada Regressiva

def derivada_regressiva(funcao,h,x):
    return (funcao(x) - funcao(x-h)) / h

h = 0.1 
x_3 = 2
dfdx_3 = derivada_regressiva(f2,h,x)
print(f'{dfdx:.3f}')
print('\n')

erro_relativo = np.abs(valor_real - dfdx_3) / np.abs(valor_real)*100
print(f'{erro_relativo}')
print('\n')

#Derivada Central

def derivada_central(funcao,h,x):
    return (funcao(x+h) - funcao(x-h)) / (2*h)

h = 0.1
x_4 = 2
dfdx_4 = derivada_central(f2,h,x)
print(f'{dfdx_4:.3f}')
print('\n')

#Gráfico

h = 0.1
x = np.arange(0,2*np.pi,h)
dfdx_5 = derivada_central(np.cos,h,x)
dfdx_6 = derivada_progressiva(np.cos,h,x)
dfdx_7 = derivada_regressiva(np.cos,h,x)

plt.figure(figsize=(12,8))
plt.plot(x,dfdx_5,label='Central')
plt.plot(x,dfdx_6,label='Progressiva')
plt.plot(x,dfdx_7,label='Regressiva')
plt.scatter(x,-np.sin(x),label='-Seno')
plt.legend()

plt.grid()
plt.show()