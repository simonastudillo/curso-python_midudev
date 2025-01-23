###
# 02 - Booleanos
# Valores lógicos: True o False
# Fundamentales para el control de flujo y la lógica en programación
###

print("\n Valores booleanos basicos:")
print("True")
print("False")

# Operadores de comparación: devuelven un valor booleano
print("\n Operadores de comparación:")
print("5 > 3", 5 > 3)     # True
print("5 < 3", 5 < 3)     # False
print("5 == 5", 5 == 5)   # True ( igualdad )
print("5 != 5", 5 != 5)   # False ( desigualdad )
print("5 >= 5", 5 >= 5)   # True ( mayor o igual )
print("5 <= 3", 5 <= 3)   # False ( menor o igual )


print("\n Comparación de cadenas:")
print("manzana < pera: ", "manzana" < "pera")   # True ( Compara lexicograficamente (letra m va antes de la letra p) )
print("Hola == hola:", "Hola" == "hola")        # True ( case sentitive )

# Operadores lógicos
print("\n Operadores lógicos:")
print("True and True", True and True)   # True
print("True and False", True and False) # False
print("True or False", True or False)   # True
print("False or False", False or False) # False
print("not True", not True)             # False
print("not False", not False)           # True