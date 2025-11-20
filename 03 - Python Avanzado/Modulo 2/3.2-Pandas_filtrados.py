
import pandas as pd # Importamos la libreria (pandas) y le agregamos el alias (pd)

# Lee el Archivo CSV
df = pd.read_csv("03 - Python Avanzado/Modulo 2/CSV_Ejemplo_1.csv") # Con la función (read_csv) de la libreria pandas, podemos leer el archivo csv

# Filtrado
filter = df["ntienda"] == "6"
df_identificador = df.where(filter).notna()
print(df_identificador)
