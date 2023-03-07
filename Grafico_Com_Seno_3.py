import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(0,2*np.pi,20)
y = np.sin(x)
plt.figure(figsize=(14,7))
plt.grid()
plt.title('Seno')
plt.plot(x,y)
plt.scatter(x,y)
plt.show()