import numpy as np 
import sympy as sp
import matplotlib.pyplot as plt

#1
pot_medida = 12.8
pot_real = 12.5
erro = np.abs(pot_real - pot_medida) / np.abs(pot_real) * 100
print(f'O erro realtivo é de {erro:.3f} %')
print('\n')

#2
def f(x):
    return x**3 - 2*x**2 + x

def derivada_progressiva(f,x,h):
    return (f(x+h) - f(x)) / h

x = 2
h = 0.01
dfdx = derivada_progressiva(f,x,h)
print(f'O valor da derivada dfdx = {dfdx:.2f}')
sp.Derivative('x**3 - 2*x**2 + x','x').doit().subs({'x':2})
print('\n')

#3
def v(t):
    return 10*t**2 - 20*t+30

def diferenca_central(f,x,h):
    return (f(x+h) - f(x-h)) / (2*h)

t = 8
h = 0.5
dvdt = diferenca_central(v,t,h)
print(f'Derivada Central: {dvdt}')
print('\n')

#4
print(sp.Derivative('10*sin(2*pi*10*t)','t').doit().subs({'t':0.5}))

def p(t):
    return 10*np.sin(2*np.pi*10*t)

t = 0.5
h = 0.005 
dvdt = diferenca_central(p,t,h)
print(f'Taxa de variação: {dvdt}')
200*np.pi
print('\n')

#5
alt = np.arange(0,3000,500, dtype=float)
temp = np.array([15,10,6,3,-1,-4], dtype=float)

##Altitude de 0 metros 
i = 0
dtda = (temp[i+1] - temp[i]) / (alt[i+1] - alt[i])
print(f'0 metros: {dtda}')

##Altitude de 1500 metros
i = 3
dtda = (temp[i+1] - temp[i-1]) / (alt[i+1] - alt[i-1])
print(f'1500 metros: {dtda}')

##Altitude de 2500 metros 
i=5
dtda = (temp[i] - temp[i-1]) / (alt[i] - alt[i-1])
print(f'2500 metros: {dtda}')
print('\n')

#6
def g(x):
    return x**2

a = 1
b = 4
n = 800
h = (b - a) / n
x = np.arange(a,b+h,h)
y = g(x)
I = h/2 * (y[0] + 2*np.sum(y[1:-1]) + y[-1])
print(I)
print('\n')

#7
def f2(x):
    return 0.1*(5 - x )*(x+1)

a = 0
b = 4 
n = 20
h = (b - a) / n
x = np.arange(a,b+h,h)
y = f2(x)
I = h/3 * (y[0] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-1:2]) + y[-1])
print(I)
print('\n')

#8
def i(t):
    return 5*np.exp(-2*t)

a = 0
b = 2 
n = 100
h = (b - a) / n
x = np.arange(a,b+h,h)
y = i(x)
I = h/2 * (y[0] + 2*np.sum(y[1:-1]) + y[-1])
print(I)
print(sp.Integral('5*E**(-2*t)',('t',0,2)).doit().simplify())
print('\n')

#9
def c(t):
    return 100 + 50 * np.sin(2*np.pi*t/24)

a = 0
b = 24 
n = 10
h = (b - a) / n
x = np.arange(a,b+h,h)
y = c(x)
I_trapz = h/2 * (y[0] + 2*np.sum(y[1:-1]) + y[-1]) 
print(I_trapz)
print('\n')

#10

def y1(t):
    return 2*np.sin(2*np.pi*5*t)

def y2(t):
    return 5*np.sin(2*np.pi*15*t)

def y3(t):
    return 10 * np.sin(2*np.pi*25*t)

t = np.linspace(0,1,1000)
sinal_1 = y1(t)
sinal_2 = y2(t)
sinal_3 = y3(t)

plt.figure(figsize=(20,12))
plt.plot(t,sinal_1, label = 'sinal 1')
plt.plot(t,sinal_2, label = 'sinal 2')
plt.plot(t,sinal_3, label = 'sinal 3')
plt.legend()
plt.title('Sinais')
plt.xlabel('tempo - s')
plt.ylabel('Amplitude')
plt.grid()
plt.show()