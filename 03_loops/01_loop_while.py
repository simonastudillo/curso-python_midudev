###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de código mientras se cumple una condición.
###

print("Bucle while")

# Bucle con una simple condición
contador = 0
while contador < 5:
  print(contador)
  contador += 1

# Utiliznando break para salir del bucle
contador = 0
while True:
  print(f"Bucle while =  {contador}")
  contador += 1
  if contador == 5:
    break

# Bucle con continue: salta la iteración actual y sigue con la siguiente
contador = 0
while contador < 10:
  contador += 1
  if contador % 2 == 0:
    continue
  print(f"Bucle continue =  {contador}")


# Else: ejecuta el bloque de código si no se cumple la condición
contador = 0
while contador < 5:
  print(f"Bucle while con else =  {contador}")
  contador += 1
else:
  print("El bucle ha terminado")

# Pedirle al usuario un número que tiene que ser positivo
# numero = -1
# while numero < 0:
#   numero = int(input("Ingrese un número positivo: "))
#   if numero < 0:
#     print("El número ingresado no es positivo")
# else:
#   print(f"El número ingresado es {numero}")

numero = -1
while numero < 0:
  try:
    numero = int(input("Ingrese un número positivo: "))
    if numero < 0:
      print("El número ingresado no es positivo")
  except:
    print("El valor ingresado no es un número")
else:
  print(f"El número ingresado es {numero}")