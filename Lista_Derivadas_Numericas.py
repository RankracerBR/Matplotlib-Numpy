#Imports 
import matplotlib.pyplot as plt 
import numpy as np 


#Funções

def f(x):
    return 2*np.exp(1.5*x)

def f2(x):
    return (x**3 - 2*np.exp(2*x)) + 4

def derivada_central(f,x,h):
    return (f(x+h) - f(x-h)) / (2*h)

def derivada_regressiva(f,x,h):
    return (f(x) - f(x-h)) / h

def derivada_progressiva(f,x,h):
    return (f(x+h) - f(x)) / h

def erro_relativo(x,h):
    return np.abs(x-h) / np.abs(h) * 100

def derivada_seno(x,h):
   return (np.sin(x) - x**2)
 
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

#1
x = 3
h = 0.1 

dydx = derivada_central(f,x,h)
print(dydx)
print('\n')

#2
erro_r = erro_relativo(x,h)
print(f'OP erro encontrado foi de: {erro_r}%')
print('\n')

#3
x = np.pi / 4 
h = np.pi / 12
f = -np.sin(x)
dydx_2 =  derivada_progressiva(np.cos,x,h)
dydx__2 = derivada_regressiva(np.cos,x,h)
dydx___2 = derivada_central(np.cos,x,h)
dydx_erro_r = erro_relativo(x,h)
print(f'*Diferença Progressiva: {dydx_2}')
print(f'*Diferença Regressiva: {dydx__2}')
print(f'*Diferença Central: {dydx___2}')
print(f'*Erro Relativo: {dydx_erro_r}')
print('\n')

#4
x = 2
h = 0.1 

derivada = derivada_seno(x,h)
erro = erro_relativo(x,h)
print(f'*Derivada Seno: {derivada}')
print(f'*Erro Relativo: {erro}')
print('\n')

#5
t = np.array([0,0.4,1,1.75,2.5])
idx = 3
p = np.array([20,100,110,161,178], dtype=float)

v_progressiva = (p[idx+1] - p[idx]) / (t[idx+1] - t[idx])
print(f'*Velocidade Progressiva: {v_progressiva}')

v_regressiva = (p[idx] - p[idx-1]) / (t[idx] - t[idx-1])
print(f'*Velocidade Regressiva: {v_regressiva}')

discreta = derivada_discreta(t,p)
print(f'*Derivada Discreta: {discreta}')
print('\n')

#6
t = np.array([0,25,50,75,100,125])
y = np.array([0,32,58,78,92,100])
derivada_2 = derivada_discreta(t,y)
print(f'*Velocidade e Aceleração: {derivada_2}')
print('\n')

#7
x = np.array([2.36,2.37,2.38,2.39])
f = np.array([0.85866,0.86289,0.86710,0.87129])

h = x[1] - x[0]
fp1 = (f[1] - f[0]) / h
fp2 = (f[2] - f[1]) / h

fp3 = (f[3] - f[2]) / h
fp4 = (f[2] - f[1]) / h

print(fp1)
print(fp3)
print('\n')

#8
x = 1
h = 0.1

progressiva = derivada_progressiva(f2,x,h)
regressiva = derivada_regressiva(f2,x,h)

print(f'*Derivada Progressiva: {progressiva}')
print(f'*Derivada Regressiva: {regressiva}')
print('\n')

#9
tempo = np.array([0,0.5,1,1.5,2])
temperatura = np.array([20.5,25.1,30.2,36.1,43.5])
pressao = np.array([101.3,103.2,106.1,110.3,116.1])

h = 0.5

dTdt_prog = np.zeros_like(temperatura)
dTdt_prog[:-1] = (temperatura[1:] - temperatura[:-1]) / h
print(f'*Derivada Progressiva(temperatura):{dTdt_prog}')

# Derivada regressiva da temperatura
dTdt_reg = np.zeros_like(temperatura)
dTdt_reg[1:] = (temperatura[1:] - temperatura[:-1]) / h
print(f'Derivada Regressiva(temperatura){dTdt_reg}')
# Derivada progressiva da pressao
dPdt_prog = np.zeros_like(pressao)
dPdt_prog[:-1] = (pressao[1:] - pressao[:-1]) / h
print(f'Derivada Progressiva(pressão){dTdt_prog}')
# Derivada regressiva da pressao
dPdt_reg = np.zeros_like(pressao)
dPdt_reg[1:] = (pressao[1:] - pressao[:-1]) / h
print(f'Derivada Regressiva(pressão):{dTdt_reg}')
print('\n')
dTdt_2 = [(temperatura[i+1] - temperatura[i-1]) / (2 * h) for i in range(1, len(temperatura)-1)]
dPdt_2 = [(pressao[i+1] - pressao[i-1]) / (2 * h) for i in range(1, len(pressao)-1)]
print(f'*Derivada Central(temperatura): {dTdt_2}')
print(f'*Derivada Central(pressão): {dPdt_2}')