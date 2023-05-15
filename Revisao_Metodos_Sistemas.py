#Imports
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
np.set_printoptions(suppress=True)

#1
def dgdl(l):
    c = 3e8
    return -c/(2*l**2) - 1

def g(l):
    f = 1e8 
    c = 3e8
    return c/(2*l) - f - l

'''Método Bisseção'''
a = 0.5
b = 2 
c = (a + b) / 2
i = 1
while np.abs(g(c)) > 0.001:
    i += 1
    if g(a)*g(c) < 0:
        b = c
    else:
        a = c
    c = (a + b) / 2

print(c,i)
print(g(c))

'''Método de Newton'''
raiz = 2
i = 1
while np.abs(g(raiz)) > 0.001:
    raiz = raiz -g(raiz) / dgdl(raiz)
    i += 1

print(raiz, i)
print('\n')

#2

def f(d):
    H = 50 
    theta = 0.1
    return H / np.tan(theta) - d

x0 = 300 
x1 = 350
i = 1
while np.abs(f(x1)) > 0.0001 and i < 100:
    x2 = x1 - f(x1)*(x1 - x0) / (f(x1) - f(x0))
    x0,x1 = x1,x2
    i += 2

print(f'A raiz aproximada é: {x1}')
print(f'Total de iterações: {i}')
print('\n')

#3

A = np.array([[1,1,1],
              [3,2,1],
              [2,3,1]], dtype = float)

print(A)

b = np.array([10,20,30])
print(b)

x = np.linalg.solve(A,b)
print(x)
print(A@x)
print('\n')

#4

A = np.array([[4,1,0,1],
              [1,4,1,0],
              [0,1,4,1],
              [1,0,1,4]], dtype = float)

B1 = np.array([15, 10, 10, 10], dtype = float)
B2 = np.array([20, 15, 15, 10], dtype = float)
B3 = np.array([25, 20, 10, 25], dtype = float)

lu_p = sp.linalg.lu_factor(A)
print(lu_p)
print('\n')

x1 = sp.linalg.lu_solve(lu_p,B1)
x2 = sp.linalg.lu_solve(lu_p,B2)
x3 = sp.linalg.lu_solve(lu_p,B3)

print(x1)
print(x2)
print(x3)
print('\n')

#Verifica se os parâmetros estão corretos
print(A@x1)
print(A@x2)
print(A@x3)