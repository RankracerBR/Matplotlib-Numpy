import matplotlib.pyplot as plt
import numpy as np

def seno_cosseno(x):
    return np.sin(x) + np.cos(x)

x = np.linspace(0,2*np.pi,100)
y1 = np.sin(x)
y2 = np.cos(x) 
y3 = seno_cosseno(x)
plt.figure(figsize=(14,7))
plt.plot(x,y1, label='Seno')
plt.plot(x,y2, label='Cosseno')
plt.plot(x,y3, label='Seno + Cosseno')
plt.title('Senoides')
plt.grid()
plt.legend()
plt.show()