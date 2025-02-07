"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""

# Para ver si un número es par
# siempre usamos el módulo %
# nos da el resto de la división: eggs % 2 == 2

def count_eggs(eggs: list) -> int:
  """
  Esta función recibe una lista de numeros enteros que representan la cantidad de huevos que han puesto diferentes dinosaurios en el parque jurásico y los de número par son de carnívoros. Devuelve un número con la suma de todos los huevos de carnívoros.
  """
  total_par_eggs = 0
  for egg in eggs:
    if egg % 2 == 0:
      total_par_eggs += egg

  return total_par_eggs

print(count_eggs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))