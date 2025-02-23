###
# 02 - Meta caracteres
# Los metacaracteres son símbolos especiales con significados específicos en las expresiones regulares.
###

import re

# 1. Punto (.)
# Coincidir con cualquier caracter excepto una nueva linea.

text = "Hola mundo, H0la de nuevo, H@la otra vez"
pattern = "H.la"
result = re.findall(pattern, text)

if result:
    print(result)
else:
  print("No se encontraron coincidencias")

text = "casa caasa cosa cisa cesa causa"
pattern = "c.sa"

matches = re.findall(pattern, text)

if matches:
  print(matches)
else:
  print("No se encontraron coincidencias")

# --------------------
# Utilizar r antes de la expresión para indicar que es una expresión regular

text = "Hola mundo, H0la de nuevo, H@la otra vez"
pattern = r"H.la"
result = re.findall(pattern, text)

if result:
    print(result)
else:
  print("No se encontraron coincidencias")

# Cómo usar la barra invertida para anular el significado especial de una símbolo
text = "Hola mundo. H0la de nuevo. H@la otra vez"
pattern = r"\."

result = re.findall(pattern, text)

if result:
  print(result)
else:
  print("No se encontraron coincidencias")


# \d: coincide con cualquier dígito (0-9)
text = "El número de teléfono es 1234567890"
pattern = r"\d"
found = re.findall(pattern, text)
print(found)


# {número}: cuantificador que coincide con exactamente n veces
text = "El número de teléfono es 1234567890"
pattern = r"\d{9}"
found = re.findall(pattern, text)
print(found)

# Ejercicio: Detectar si hay un número de España en el texto gracias al prefijo +34
text = "El número de teléfono es +34 688999999 aúntalo vale?"

pattern = r"\+34 \d{9}"
found = re.search(pattern, text)
print(found)

# \w: coincide con cualquier caracter alfanumerico (a-z, A-Z, 0-9, _)
text = "el_ribuis_69@-"
pattern = r"\w"
found = re.findall(pattern, text)
print(found)

# \s: Coincide con cualquier espacio en blaco, tabulación, salto de linea
text = "Hola mundo\n¿Cómo estás?\t"
pattern = r"\s"

matches = re.findall(pattern, text)
print(matches)

# ^: Coincide con el principio de una cadena
text = "@423_name"
pattern = "^\w" #Validar nombre de usuario
found = re.findall(pattern, text)
print(found)

phone = "+34 688999999"
pattern = r"^\+\d{1,3} \d{9}"

valid = re.search(pattern, phone)
print(valid)

# $: Coincide con el final de una cadena
text = "Hola mundo"
pattern = "mundo$"
found = re.search(pattern, text)
print(found)

# Ejercicio: valida que un correo sea de gmail
text = "miduga@gmail.com"
pattern = r"@gmail\.com$"
found = re.search(pattern, text)
print(found)

# Ejercicio: Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extension .txt
files = "file1.txt file2.txt file3.csv file2.pdf midu-of.webp secret.txt"
pattern = r"\.txt$"
found = re.findall(pattern, files)
print(found)

# \b: coincide con el principio o final de una palabra
text = "casa casada cosa cosas casado casa"
pattern = r"\bc.sa\b"

matches = re.findall(pattern, text)
print(matches)

# |: Coincidir con una opción u otra
fruits = "platano, manzana, aguacate, palta, pera, tamarindo"
pattern = r"aguacate|palta|\b\w{7}\b"
found = re.findall(pattern, fruits)
print(found)