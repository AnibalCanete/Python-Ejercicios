
# Importamos las librerias (matplotlib) y (numpy) 
import matplotlib.pyplot as plt
import numpy as np

# Creamos la variable (xpoints) utilizando la libreria (numpy) creamos una lista con los valores (1, 8)
xpoints = np.array([1, 8])
print(xpoints) # Imprimimos la variable
ypoints = np.array([3, 10]) # Creamos la variable (ypoints) utilizando la libreria (numpy) creamos una lista con los valores (3, 10)
print(ypoints) # Imprimimos la variable

plt.plot(xpoints, ypoints) # Utilizamos la función (plot) para crear el grafico
plt.show() # Con la libreria (matplotlib) utilizamos la función (show()) para porder ver el grafico
