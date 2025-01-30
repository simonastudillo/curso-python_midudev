###
# EJERCICOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

numbero1: int = int(input("Ingrese un número: \n"))
numbero2: int = int(input("Ingrese un segundo número: \n"))

if numbero1 > numbero2:
    print(f"El número 1 ({numbero1}) es mayor que el número 2 ({numbero2})")
elif numbero1 < numbero2:
    print(f"El número 2 ({numbero2}) es mayor que el número 1 ({numbero1})")
else:
    print(f"Los números son iguales")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

numbero1: int = int(input("Ingrese un número: \n"))
numbero2: int = int(input("Ingrese un segundo número: \n"))
operación: str = input("Ingrese un simbolo de operación (+, -, *, /): \n")

if operación == "+":
    print(f"El resultado de {numbero1} + {numbero2} es {numbero1 + numbero2}")
elif operación == "-":
    print(f"El resultado de {numbero1} - {numbero2} es {numbero1 - numbero2}")
elif operación == "*":
    print(f"El resultado de {numbero1} * {numbero2} es {numbero1 * numbero2}")
elif operación == "/":
    if numbero2 == 0:
        print(f"No se puede dividir por cero")
    else:
        print(f"El resultado de {numbero1} / {numbero2} es {numbero1 / numbero2}")

print(f"El resultado de {numbero1} {operación} {numbero2} es {eval(f'{numbero1} {operación} {numbero2}')}")


# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

year: int = int(input("Ingrese un año: \n"))
if year % 4 == 0:
  if year & 100 == 0:
      if year % 400 == 0:
          print(f"El año {year} es bisiesto")
      else:
          print(f"El año {year} no es bisiesto")
  else:
      print(f"El año {year} es bisiesto")
else:
  print(f"El año {year} no es bisiesto")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

age: int = int(input("Ingrese su edad: \n"))
if age > 64:
  print("Eres adulto mayor")
elif age > 17:
  print("Eres adulto")
elif age > 12:
  print("Eres adolescente")
elif age > 2:
  print("Eres niño")
else:
  print("Eres bebé")