import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 4*x + 3.5

def bissecao(f,a,b,tol,max_iter):
    assert f(a)*f(b) < 0, 'Não há convergência garantida'
    iteracao = 1 
    c = (a + b) / 2
    while np.abs(f(c)) > tolerancia and iteracao < max_iter:
        iteracao +=1
    if f(a)+f(c) < 0:
        b = c
    else:
        a = c
    c = (a + b) / 2
    return c

x = np.linspace(0,4,1000)
y = f(x)
plt.plot(x,y)
plt.axhline(y=0,color='black')
plt.axvline(x=1,color='red')
plt.axvline(x=2,color='red')
plt.grid()
plt.show()

#
a = 1
b = 2
tolerancia = 1e-6
iteracao = 1
c = (a + b) / 2
while np.abs(f(c)) > tolerancia:
    iteracao +=1
    if f(a)+f(c) < 0:
        b = c
    else:
        a = c
    c = (a + b) / 2

print(f'Iterações: {iteracao}')    
print(f'A raiz da equação é: {c}')

#
raiz = bissecao(f,1,2,1e-6,100)
print(raiz)

#
def g(freq):
    L = 0.5e-3 
    C = 0.2e-6
    return 2 * np.pi*freq*L - 1 / (2*np.pi*freq*C)

f1 = 10e3
f2 = 20e3

x = np.linspace(f1,f2,1000) 
y = g(x)

plt.plot(x,y)
plt.axhline(y=0,color='black')
plt.grid()
plt.show()

raiz = bissecao(g,14e3,17e3,1e-6,100)
print(raiz)

g(raiz)