
import pandas as pd # Importamos la libreria (pandas) y la agregamos un alias (pd)

# Leemos el archivo CSV
df = pd.read_csv("03 - Python Avanzado/Modulo 2/CSV_Ejemplo_1.csv") # Con la función (read_csv) de la libreria pandas, podemos leer el archvio csv

# Acceso por posición de filas
print(df[0:3]) # Imprimimos los datos desde la posición 0 hasta la posición antes de la posición 3

# Acceso por Columnas
print(df[["dia", "ntienda", "nalmacen"]])
