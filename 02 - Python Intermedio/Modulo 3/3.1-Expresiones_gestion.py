
# La gestión de errores, es que apesar de que salga dicho error el programa siga compilando

# ZeroDivisionError
try:
    resultado = 10 - (1/0)
except:
    print("Error de Sintaxis")

# NameError
try:
    print(4 + spam * 3)
except:
    print("Error de NameError")

# TypeError
try:
    resultado = "2" + 2
except:
    print("Error de TypeError")

