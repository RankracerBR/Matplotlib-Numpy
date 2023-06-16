import numpy as np
import matplotlib.pyplot as plt

def aprox_e(x, n_termos=10):
    aprox = 0
    for n in range(n_termos):
        aprox += x**n / np.math.factorial(n)
    return aprox

n = 0
valor_anterior = aprox_e(1,n)
erro = float('inf')
erros_calculados = []
while erro > 0.5:
  n += 1
  valor_atual = aprox_e(1,n)
  erro = np.abs(valor_atual - valor_anterior) / np.abs(valor_atual) * 100
  erros_calculados.append(erro)
  valor_anterior = valor_atual

print(f'Total de termos : {n} termos')
print(f'Valor aproximado: {valor_atual}')
print(f'Valor real: {np.exp(1)}')