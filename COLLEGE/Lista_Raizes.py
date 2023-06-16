#Imports 
import numpy as np 
import matplotlib.pyplot as plt

#1 
def f(x):
    return x**3 - 20

def bissecao(f,a,b,tol=0.00001, max_iter=100): 
  if f(a) * f(b) > 0:
    print('Não há convergência garantida')
  c = (a + b) / 2
  i = 1
  while np.abs(f(c)) > tol and i < max_iter:
    if f(a) * f(c) < 0:
      b = c
    else:
      a = c 
    c = (a + b) / 2
    i += 1
    return c

raiz_bissecao = bissecao(f,1,4)
print(raiz_bissecao)
print('\n')

#2
def f2(x):
    return np.sin(10*x) + np.cos(3*x)

raiz_bissecao_2 = bissecao(f2,5.5,6.0)
print('\n')

#3
def f3(x):
    return np.sin(10*x) + np.cos(3*x)

def df2(x):
    return 0.1736*x + 0.9848 * x

def newton(f,df,x,tol=0.0001,max_iter = 100):
  i = 1
  while np.abs(f(x)) > tol and i < max_iter:
    x = x - f(x) / df(x)
    i += 1
  return x

raiz_newton = newton(f3,df2,5.5)
print(f'> Valor em Newton: {raiz_newton}')
print(f'> Valor na Bisseção: {raiz_bissecao}')
print('\n')

#4
def f4(x):
    return x**3 - 20

def df3(x):
    return 3*x**2 - 20

raiz_newton_2 = newton(f4,df3,4.0)
print(raiz_newton_2)
print('\n')

#5
def f5(x):
    return x**3 - 20

def secante(f,x0,x1,tol=0.0001,max_iter=100):
    i = 1
    while (np.abs(f(x1))) > tol and i <max_iter:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0,x1 = x1,x2
        i += 1
    return x1

raize_secante = secante(f5,1.0,4.0)
print(raize_secante)
print('\n')

#6
def f6(x):
    return x**2 - 13

def df6(x):
    return 2 * x

raize_newton = newton(f6,df6,13,tol = 1e-15, max_iter=200)
print(raiz_newton)