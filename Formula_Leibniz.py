import numpy as np
import matplotlib.pyplot as plt

def pi_aproximado(n):
    acc = 0
    den = 1
    for i in range(n):
        if i % 2 == 0:
            acc += 1 / den
        else:
            acc -= 1 / den 
    return 4 * acc    

print('_'*30)

print(f'{pi_aproximado(10)}')
print(f'{pi_aproximado(100)}')
print(f'{pi_aproximado(1000)}')
print(f'{pi_aproximado(10000)}')

print('_'*30)
print('Comparação:')

valor_pi = np.pi

valor_1 = 10
erro_absoluto = np.abs(valor_pi - valor_1)
erro_relativo = np.abs(valor_pi - valor_1) / np.abs(valor_pi)
print(f'O erro absoluto do valor 1n: {erro_absoluto}')
print(f'O erro relativo do valor 1n: {erro_relativo}%')
print('-'*30)

valor_2 = 100
erro_absoluto_2 = np.abs(valor_pi - valor_2)
erro_relativo_2 = np.abs(valor_pi - valor_2) / np.abs(valor_pi)
print(f'O erro absoluto do valor 2n: {erro_absoluto_2}')
print(f'O erro relativo do valor 2n: {erro_relativo_2}%')
print('-'*30)

valor_3 = 1000
erro_absoluto_3 = np.abs(valor_pi - valor_3)
erro_relativo_3 = np.abs(valor_pi - valor_3) / np.abs(valor_pi)
print(f'O erro absoluto do valor 3n: {erro_absoluto_3}')
print(f'O erro relativo do valor 3n: {erro_relativo_3}%')
print('-'*30)

valor_4 = 10000
erro_absoluto_4 = np.abs(valor_pi - valor_4)
erro_relativo_4 = np.abs(valor_pi - valor_4) / np.abs(valor_pi)
print(f'O erro absoluto do valor 4n: {erro_absoluto_4}')
print(f'O erro relativo do valor 4n: {erro_relativo_4}%')
print('-'*30)