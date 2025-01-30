###
# 04 - Functions
# Bloques de código reutilizables y parametrizables
###

"""
Definición de una función

def nombre de la función (parametro1, parametro2, ...):
    # docstring
    # código
    return valor #Opcional
"""

def saludar():
  print("Hola")

saludar()

def saludar_a(nombre):
  print(f"Hola {nombre}")

saludar_a("Juan")
saludar_a("Pepe")

def sumar(a, b):
  return a + b

result = sumar(1, 2)
print(result)
print(sumar(1, 2.5))

# Documentar las funciones
def restar(a:int, b:int) -> int:
  """Restar dos números y devuelve el resultado"""
  return a - b

print(restar(10, 2))

# Parametros por defecto
def multiplicar(a:int, b:int=2) -> int:
  """Multiplicar dos números y devuelve el resultado"""
  return a * b

print(multiplicar(10))
print(multiplicar(10, 3))

# Argumentos por clave
def describir_persona(nombre, edad, sexo):
  print(f"{nombre} tiene {edad} años y es {sexo}")

describir_persona("Juan", 20, "masculino") # por posición
describir_persona(nombre="Pepe", sexo="femenino", edad=15) # argumentos por clave

# Argumentos de longitud de variable
def sumar_lista(*lista):
  suma = 0
  for elemento in lista:
    suma += elemento
  return suma

print(sumar_lista(1, 2, 3, 4, 5))

# argumentos de clave-valor y de longitud de variable
def mostrar_informacion_de(**kwargs):
  for key, value in kwargs.items():
    print(f"{key}: {value}")

mostrar_informacion_de(nombre="Juan", edad=20, sexo="masculino")
mostrar_informacion_de(country="Chile", edad=15, nombre="Pepe")