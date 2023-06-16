import matplotlib.pyplot as plt 
import numpy as np

notas = np.array([8,7,9,10,6])
disciplinas = np.array(['Matemática','Português','Física','Química','História'])

plt.figure(figsize=(14,7)) 
plt.barh(disciplinas,notas)
plt.grid()
plt.xlabel('Disciplinas')
plt.ylabel('Notas')
plt.title('Notas do Semestre')
plt.show()