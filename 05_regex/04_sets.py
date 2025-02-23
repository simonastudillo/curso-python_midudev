import re

# []: Coincide con cualquier caracter de los corchetes
username = "rub.ius$_69+"
pattern = r"^[\w._%+-]+$"
matches = re.search(pattern, username)
print(matches)
if matches:
  print("Usuario válido")
else:
  print("Usuario inválido")

# Ejercicio 1:
# Buscar todas las vocales de una palabra
text = "Hola mundo"
pattern = r"[aeiou]"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio 2:
# Una regex para encontrar las palabras man, fan y ban pero ignora el resto
text = "man ran fan ñan ban"
pattern = r"[mfb]an"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio 3:
# Nos han complicado el asunto, porque ahora hay palabras que encajan pero no empiezan o terminan por esas letras. Solo queremos las palabras man, fan y ban
text = "omniman ran fan ñan bandana"
pattern = r"\b[mfb]an\b"
matches = re.findall(pattern, text)
print(matches)


# r"[1-2]" del 1 al 2
# r"[a-z]" del a al z
# r"[A-Z]" del A al Z
# r"[0-9]" del 0 al 9
# r"[a-zA-Z]" de la a a la z y de la A a la Z
# r"[a-zA-Z0-9]" de la a a la z, de la A a la Z y del 0 al 9

# [^]: coincide con cualquier caracter que no esté en los corchetes
text = "Hola mundo"
pattern = r"[^aeiou]"
matches = re.findall(pattern, text)
print(matches)