###
# 01 - Sentencias condicionales
# Permiten ejecutar bloques de código solo si se cumple una condición
###

import os

os.system("cls")

print("\r sentencia simple condicional")

edad = 18

if edad >= 18:
  print("Eres mayor de edad")
  print("¡Felicidades!")
else:
  print("Eres menor de edad")
  print("Lo siento")
  
print("\n Sentencia condicional con elif")

nota = 7

if nota >= 9:
  print("¡Sobresaliente!")
elif nota >= 7:
  print("Notable")
elif nota >= 5:
  print("Aprobado")
else:
  print("No se ha aprobado")

print("\n Condiciones multiples")
edad = 25
tiene_carnet = True

if edad >= 18 and tiene_carnet:
  print("Puedes conducir")
else:
  print("No puedes conducir")


print("\n Un pueblo de Isla Margarita")

if edad >= 18 or tiene_carnet:
  print("Puedes conducir")
else:
  print("Paga al policia y puedes conducir")

es_fin_de_semana = False

if not es_fin_de_semana:
  print("¡Felicidades!")
else:
  print("¡Buenas noches!")

print("\n Anidar condicionales")

edad = 20
tiene_dinero = True

if edad >= 18:
  if tiene_dinero:
    print("Puedes ir a la disco!")
  else:
    print("¡No tienes dinero!")
else:
  print("¡No puedes ir!")

# Más facil
if edad < 18:
  print("¡No puedes ir!")
elif tiene_dinero:
  print("Puedes ir a la disco!")
else:
  print("¡No tienes dinero!")

numero = 5
if numero:
  print("El número es distinto de cero")

nombre = "Juan"
if nombre:
  print("El nombre es distinto a vacío")

numero = 3
es_el_tres = numero == 3
if es_el_tres:
  print("El número es 3")


print("\n La condición ternaria")
# Es una forma concisa de hacer un if-else
# [código si cumple la condición] if [condición] else [código que no cumple]}

edad = 17
print("Es mayor de edad") if edad >= 18 else print("Es menor de edad")