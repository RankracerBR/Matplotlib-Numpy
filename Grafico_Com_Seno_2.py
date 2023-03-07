import matplotlib.pyplot as plt 
import numpy as np 

x = np.arange(0,2*np.pi,np.pi/32)
y = np.sin(x)
plt.grid()
plt.title('Seno')
plt.plot(x,y)
plt.scatter(x,y)
plt.show()