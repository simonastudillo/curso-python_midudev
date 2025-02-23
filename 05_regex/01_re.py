##
# 01 - Expresiones regulares
#
# Crear expresiones regulares son uns secuencia de caracteres que formanun patrón de búsqueda.  Se utilizan para la búsqueda de cadenas de texto, validación de datos, etc.
# ¿Por qué aprender Regex?
#  - Búsqueda avanzada: Encontrar patrones especificos en textos grandes en textos grandes de forma rápida y precisa. (un editor de Markdown sólo usando Regex)
#  - Validación de datos: Asegurarte que los datos que ingresa un usuario como el email, teléfono, etc. son correctos.
#  - Manipulación del texto: Extraer, reemplazar y modificar partes de la cadena de texto fácilmente.

import re # Importamos el módulo de expresiones regulares

# Crear un patrón, que es una cadena de texto que describe lo que queremos encontrar.
pattern = "hola"

# Texto que queremos buscar
text = "hola mundo"

# Usar la función de busqueda de re
result = re.search(pattern, text)

# Imprimir el resultado
if result:
  print(result)
else:
  print("No se encontró el patrón")

# group() devuelve la cadena que coincide con el pattern
print(result.group())

# .start() devolver la posición inicial de la coincidencia
print(result.start())

# .end() devolver la posición final de la coincidencia
print(result.end())

# .span() devolver la posición inicial y final de la coincidencia
print(result.span())


# Ejercicio 1
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto e indica en que posición empieza y termina la coincidencia.
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo laa puede cagar con las Regex para ir con cuidado con la IA."

pattern = "IA"

found_ia = re.search(pattern, text)

if found_ia:
  print(found_ia.group())
  print(found_ia.start())
  print(found_ia.end())
  print(found_ia.span())
else:
  print("No se encontró la palabra IA")

# Encontrar todas las coincidencias de un patrón
text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python."
pattern = "Python"

matches = re.findall(pattern, text)

print(matches)

# iter() devuelve un iterador que contiene todos los resultados de la búsqueda
pattern = "Python"

matches = re.finditer(pattern, text)

for match in matches:
  print(match.group())
  print(match.start())
  print(match.end())
  print(match.span())
  

#Ejercicio 2
# Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto e indica en que posición empieza y termina cada coincidencia y cuantas veces se encontró.
text = "Este en el curso de Python de midudev. ¡Suscríbete! a midudev si te gusta este contenido ! midu"
pattern = "midu"

matches = re.finditer(pattern, text)

cantidad = 0

for match in matches:
  print(match.group(), match.start(), match.end())
  cantidad += 1

print(f"Encontradas {cantidad} coincidencias")