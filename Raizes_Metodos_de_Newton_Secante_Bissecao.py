import numpy as np
import matplotlib.pyplot as plt

#
def p(x):
    return -0.6*x**2 + 2.4*x + 5.5

def dp(x):
    return -1.2*x + 2.4

raiz = 10
i = 1
while np.abs(p(raiz)) > 0.0001 and i < 100:
    raiz = raiz - p(raiz) / dp(raiz)
    i += 1
print(f'A raiz aproximada é: {raiz}')
print(f'Total de iterações: {i}')
print('\n')

x = np.linspace(-5,7,1000)
y = p(x)
plt.plot(x,y)
plt.axhline(y = 0, color='black')
plt.axvline(x = raiz, color='red')
plt.grid()
plt.show()

#
x0 = 10
x1 = 12
while np.abs(p(x1)) > 0.0001 and i < 100:
    x2 = x1 - p(x1)*(x1 - x0) / (p(x1) - p(x0))
    x0,x1 = x1,x2
    i += 1
print(f'A raiz aproximada é: {x1}')
print(f'Total de iterações: {i}')
print('\n')

#
def f(x):
    return x**3 - 6*x**2 + 11*x - 6

def df(x):
    return 3*x**2 - 12*x + 11

def newton(f,df,x,tol=0.0001,max_iter=100):
    i = 1
    while np.abs(f(x)) > tol and i < max_iter:
        x = x - f(x) / df(x)
        i += 1
    return x

def secante(f,x0,x1,tol=0.0001, max_iter=100):
    i = 1
    while(np.abs(f(x1))) > tol and i < max_iter:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0,x1 = x1,x2
        i += 1
    return x1

def bissecao(f,a,b,tol=0.0001,max_iter=100):
    if f(a)*f(b) > 0:
        print('Não há convergência garantida')
    c = (a + b) / 2
    i = 1
    while np.abs(f(c)) > tol and i < max_iter:
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
        c = (a + b) / 2
        i += 1
    return c 

raiz_newton = newton(f,df,4)
print(raiz_newton)

raiz_secante = secante(f,2.5,4)
print(raiz_secante)

raiz_bissecao = bissecao(f,2.5,4)
print(raiz_bissecao)
print('\n')

x = np.linspace(0,4,100)
y = f(x)
plt.plot(x,y)
plt.axhline(y = 0, color = 'blue')
plt.axvline(x = raiz_newton, color = 'blue')
plt.axvline(x = raiz_bissecao, color = 'green')
plt.axvline(x = raiz_secante, color='red')
plt.grid()
plt.show()

#
def f2(x):
    return x**2 - 72

def df2(x):
    return 2*x

raiz = newton(f2,df2,72,tol=1e-15)
print(raiz)