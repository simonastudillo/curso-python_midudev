
list1 = [1, 2, 3, 4, 5]

# Añadir elemento al final
list1.append(6)
print(list1)

# Añadir elemento en posición en concreto
list1.insert(1, 10)
print(list1)

# Añadir varios elementos al final
list1.extend([7, 8, 9])
print(list1)

# Eliminar elemento que coincida con un valor (solo 1 elemento)
list1.remove(10)
print(list1)

#  Eliminar por indice o el último de la lista
list1.pop()
print(list1)

list1.pop(0)
print(list1)

# Eliminar elemento con delete
del list1[0]
print(list1)

# Eliminar un rango de elementos
del list1[1:3]
print(list1)

# Eliminar todos los elementos de una lista
list1.clear()
print(list1)

# Ordenar listas
list1 = [13, 10, 2, 8, 99, 101]
list1.sort()
print(list1)

# Crear lista ordenada
list1 = [13, 10, 2, 8, 99, 101]
sorted_list = sorted(list1)
print(sorted_list)

frutas = ["Manzana", "pera", "naranja", "limón", "manzana", "pera"]
frutas.sort()
print(frutas)

frutas.sort(key=str.lower)
print(frutas)

frutas = ["manzana", "pera", "naranja", "limón", "manzana", "pera"]
frutas.sort()
print(frutas)

list1 = [13, 10, 2, 8, 99, 101, 13]
print( list1.count(13)) 

print( 13 in list1)