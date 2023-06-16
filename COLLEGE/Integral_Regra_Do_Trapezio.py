import numpy as np 

def f(x):
    return x**2

def g(x):
    return np.sin(x)

def trapezio(x,y,h):
    return (h/2) * (y[0] + 2*np.sum(y[1:-1]) + y[-1])

a = 0
b = 1
n = 100
h = (b - a) / n
x = np.arange(a,b+h,h)
y = f(x)
integral = (h/2)*(y[0] +2*np.sum(y[1:-1]) + y[-1])
print(f'>O valor da integral de x**2 no intervalo[0,1] é: {integral}')
print('\n')

a = 0
b = np.pi/2 
n = 10
h = (b - a) / n
x = np.arange(a,b+h,h)
y = g(x)
integral_2 = (h/2) * (y[0] + 2*np.sum(y[1:-1]) + y[-1])
print(f'>O valor da integralseno(x) no intervalo[0,π/2] é: {integral_2}')
print('\n')

a = 0
b = np.pi /2
n = 1
h = (b-a)/n
x = np.arange(a,b+h,h)
y = g(x)
valor_anterior = trapezio(x,y,h)
erro = float('inf')

while erro > 0.005:
  n += 1
  h = (b - a) / n
  x = np.arange(a,b+h,h)
  y = g(x)
  valor_atual = trapezio(x,y,h)
  erro = np.abs(valor_atual - valor_anterior) / np.abs(valor_atual) * 100
  valor_anterior = valor_atual
  
print(f'>A quantidade mínima de intervalos: {n}')
print(f'>Aproximação da integral: {valor_atual}')