import numpy as np
import matplotlib.pyplot as plt


def aprox_e(x, n_termos= 10):
    aprox = 0
    for n in range(n_termos):
        aprox += x**n / np.math.factorial(n)
    return aprox

e_real = np.exp(1)
print(e_real)

e_aproximado = aprox_e(1,5)
print(e_aproximado)

print(np.abs(e_real - e_aproximado))