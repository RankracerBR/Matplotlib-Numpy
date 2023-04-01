#Imports
import numpy as np

#Funções
def fx(x):
    return x**3 - 2*x + 1

def trapezio(x,y,h):
    return (h/2)*(y[0]+ 2*np.sum(y[1:-1]) + y[-1])

def g(x):
    return np.cos(x)

def fx2(x):
    return 1/(x+1)

def fh(a,b,n):
    return (b - a) / n

def fx3(x):
    return 1 - np.exp(-x)

def fx4(x):
    return x**2

def fx5(x):
    return 8 + 4*(np.cos(x))

def simpson(f,a,b,n):
  assert n % 2 == 0, 'Quantidade inválida de intervalos'

  h = (b - a) / n
  x = np.arange(a,b+h,h)
  y = f(x)
  integral = (h/3) * (y[0] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-1:2]) + y[-1])
  return integral 

def fx6(x):
  return 0.2 + 25*x + 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5

def fx7(x):
  return x**3 - 2*x + 1

#1
a = 0 
b = 2 
n = 4

h = fh(a,b,n)
x = np.arange(a,b+h,h)
y = fx(x)
trape = trapezio(x,y,h)
print(f'1- {trape}')
print('\n')


#2
a = -np.pi/2
b = np.pi/2 
n = 1000000
h = fh(a,b,n)

x = np.arange(a,b+h,h)
y = g(x)
trape_2 = trapezio(x,y,h)
print(f'2- {trape_2}')
print('\n')

#3
a = 0
b = 2
n = 10

h = fh(a,b,n)
x = np.arange(a,b+h,h)
y = fx2(x)
trape_3 = trapezio(x,y,h)
print(f'3- {trape_3}')
print(f'Verificação Analítica(3): {np.log(3)}')
print('\n')

#4
a = -2 
b = 4
n = 100

h = fh(a,b,n)
x = np.arange(a,b+h,h)
y = fx3(x)

trape_4 = trapezio(x,y,h)
print(f'4- {trape_4}')
print('\n')

#5
a = 0
b = 1
n = 100

h = fh(a,b,n)
x = np.arange(a,b+h,h)
y = fx4(x)

trape_5 = trapezio(x,y,h)
print(f'5- {trape_5}')
print('\n')

#6
a = 0 
b = np.pi/2 
n = 10

h = fh(a,b,h)
x = np.arange(a,b+h,h) 
y = fx5(x)

trape_6 = trapezio(x,y,h)
print(f'6- {trape_6}')
print('\n')

#7
simp1 = simpson(fx5,0,np.pi/2,10)
print(f'7- Comperação: Trapézio: {trape_6}, Simpson: {simp1}')
print('\n')

#8
simp2 = simpson(fx6,0,0.8,10)
print(simp2)
print('\n')

#9
simp3 = simpson(fx7,0,2,10)
print(simp3)