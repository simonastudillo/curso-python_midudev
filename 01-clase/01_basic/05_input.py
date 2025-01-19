###
# 05 - Input
# La función input() nos permite leer datos de la consola
###

print("Ingrese su nombre")
nombre = input()
print(f"Hola {nombre}, encantado de conocerte")

edad = input("Ingrese su edad: \n")
print(f"Tu edad es {edad}")
print(f"Dentro de 20 años tendrás {int(edad) + 20} años")

print("Obtener múltiples valores")
country, city = input("¿En qué pais y ciudad vives?: \n").split()
print(f"Tu country es {country}")
print(f"Tu city es {city}")