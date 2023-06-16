import numpy as np

def f(x):
  return x**2

def g(x):
  return np.sin(x)

def simpson(f,a,b,n):

  assert n % 2 == 0, 'Quantidade inválida de intervalos'

  h = (b - a) / n
  x = np.arange(a,b+h,h)
  y = f(x)
  integral = (h/3) * (y[0] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-1:2]) + y[-1])
  print(integral)

a = 0
b = 1
n = 2
h = (b - a) / n
x = np.arange(a,b+h,h)
y = f(x)
integral = (h/3) * (y[0] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-1:2]) + y[-1])
print(f'A integral de x**2 no intervalo [0,1] é {integral}')
 
a = 0
b = np.pi / 2
n = 10
h = (b - a) / n
x = np.arange(a,b+h,h)
y = g(x)
integral = (h/3) * (y[0] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-1:2]) + y[-1])
print(f'A integral de sin(x) no intervalo [0,pi/2] é {integral}')


simpson(g,0,np.pi/2,4)