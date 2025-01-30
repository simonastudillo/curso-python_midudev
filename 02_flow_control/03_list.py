###
# 03 - Listas
# Listas son secuencias ordenadas de elementos
###

print("\n Crear listas")

lista1 = [1, 2, 3, 4, 5]
lista2 = ["uno", "dos", "tres"]
lista3 = ["uno", 2, True]
listaVacia = []
lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(lista1)
print(lista2)
print(lista3)
print(listaVacia)
print(lista_de_listas)

# Acceso a elementos por índice
print(lista2[0])
print(lista2[1])
print(lista2[-1])

print(lista_de_listas[0][0])

# Slicing (rebanado) de listas
print( lista1[1:3] )
print( lista1[1:-1] )
print( lista1[1:] )
print( lista1[:3] )
print( lista1[-3:] )
print( lista1[:] )

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print( lista1[::2] )
print( lista1[::-1] )

# Cambiar elementos
lista1[0] = 20
print(lista1)

# Añadir elementos
lista1 += [11, 12, 13]
print(lista1)

print( len(lista1) );