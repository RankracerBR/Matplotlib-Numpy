import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi]) 
y = np.sin(x)
plt.figure(figsize=(14,7))
plt.grid()
plt.title('Seno')
plt.plot(x,y)
plt.scatter(x,y)
plt.show()