
# Recordar instalar la libreria (pandas) en Python o en nuestro editor de texto, podemos instalarlo en la terminal con (pip install pandas) 
import pandas as pd # Importamos la libreria (pandas) y le colocamos un alias (pd)

# Lee el Archivo CSV
# df significa DataFrame - Tipo de Dato Propio de Pandas
df = pd.read_csv("03 - Python Avanzado/Modulo 2/CSV_Ejemplo_1.csv") # Con la función (read_csv) de la libreria pandas, podemos leer el archivo csv

# Muestra las Primeras Filas
# print(df.head()) # Imprimimos la variable (df), con la función (head()), podemos ver los primeros cinco elementos de la tabla
print(df) # Imprimimos la variable (df)
