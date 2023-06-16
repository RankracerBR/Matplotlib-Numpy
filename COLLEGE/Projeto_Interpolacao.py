import numpy as np 
from scipy.interpolate import lagrange, interp1d
import matplotlib.pyplot as  plt


frota_veiculos = np.array([45029257,49644025,59361642,64817974,70543535,76137191,81600729,86700490,90686936,93867016,97091956,100746553,104784375,107948371,111446870,115116532], dtype = float)
anos = np.array([2006,2007,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022], dtype = float)

#Aplicação da Formula de Lagrange
poly_lagrange = lagrange(frota_veiculos,anos)
anos_novo = np.linspace(2006,2022)
frota_veiculos_novo = poly_lagrange(anos_novo)

#Gráfico com Lagrange
plt.scatter(frota_veiculos, anos)
plt.plot(anos_novo,frota_veiculos_novo)
plt.plot(frota_veiculos_novo,poly_lagrange(frota_veiculos_novo))
plt.grid()
plt.show()

#Spline
spline = interp1d(anos,frota_veiculos, kind='cubic')
anos_2_novo = np.linspace(2006,2022)
frota_veiculos_2_novo = spline(anos_2_novo)

#Gráfico com Spline
plt.scatter(anos,frota_veiculos, c='red')
plt.plot(anos_2_novo,frota_veiculos_2_novo)
plt.grid()
plt.show()