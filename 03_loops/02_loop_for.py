###
# 02 - Bucles (for)
# Permiten ejecutar un bloque de código mientras ITERA sobre un iterable o una lista
###

print("Bucle for")

# Iterar una lista
frutas = ["manzana", "pera", "banana", "naranja"]
for fruta in frutas:
  print(fruta)

# Iterar sobre cualquier tipo de iterable
cadena = "simon"
for caracter in cadena:
  print(caracter)

# enumerate(): Permite iterar sobre un iterable y devolver un índice y un elemento
frutas = ["manzana", "pera", "banana", "naranja"]
for indice, fruta in enumerate(frutas):
  print(f"indice = {indice}, fruta = {fruta}")


# bucles anidados
letras = ["A", "B", "C"]
numeros = [1, 2, 3]
for letra in letras:
  for numero in numeros:
    print(f"{letra}{numero}")

# break: Salir del bucle
animales = ["gato", "perro", "raton", "elefante", "lobo"]
for index, animal in enumerate(animales):
  print(animal)
  if animal == "elefante":
    print(f"El índice del animal es {index}")
    break

# conituar: Salir del bucle y continuar con el siguiente
animales = ["gato", "perro", "raton", "elefante", "lobo"]
for index, animal in enumerate(animales):
  if animal == "elefante":
    continue
  print(animal)

# Comprensión de listas (list comprehension)
animales = ["gato", "perro", "raton", "elefante", "lobo"]
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

# Muestra los números pares de una lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = [numero for numero in numeros if numero % 2 == 0]
print(numeros_pares)