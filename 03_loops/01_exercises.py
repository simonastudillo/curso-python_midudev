###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

contador = 10
while contador > 0:
  print(contador)
  contador -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

suma = 0
contador = 1
while contador <= 20:
  if contador % 2 == 0:
    suma += contador
  contador += 1

print(suma)

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

numero = int(input("Introduzca un número entero positivo: "))
original = numero
factorial = 1
while numero > 0:
  factorial *= numero
  numero -= 1

print(f"El factorial de {original} es {factorial}")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

while True:
  contrasena = input("Introduzca una contraseña: ")
  if len(contrasena) >= 8:
    print("Contraseña válida")
    break
  else:
    print("La contraseña debe tener al menos 8 caracteres")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

multiplo = int(input("Introduzca un número: "))
contador = 1
while contador <= 10:
  print(f"{contador} x {multiplo} = {contador * multiplo}")
  contador += 1

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")

numero_n = int(input("Introduzca un número entero positivo: "))
original = numero_n
while numero_n > 0:
  if original % numero_n == 0:
    print(f"{numero_n} es un número primo")
  numero_n -= 1