##
# 03 - Quantifiers
# Los cuantificadores se utilizan para especificar cuántas ocurrencias de un carácter o grupo de caracteres se deben encontrar en una cadena.
##

import re

# *: Puede aparecer 0 o más veces
text = "aaaba"
pattern = "a*"
result = re.findall(pattern, text)
print(result)

# Ejercicio 1:
# ¿Cuántas palabras tienen de 0 a más "a" y despues una b?

text = "aaaba abba aabbaa"
pattern = "a*b"
result = re.findall(pattern, text)
print(result)

# +: Puede aparecer 1 o más veces
text = "dddd aaaa ccc bb"
pattern = "a+"
result = re.findall(pattern, text)
print(result)

# ?: Puede aparecer 0 o 1 vez
text = "aaabacb"
pattern = "a?b"
result = re.findall(pattern, text)
print(result)

# Ejercicio 2:
# Haz opcional que aparezca un +34 en el siguiente texto
text = "34 688999999"
pattern = r"(\+|00)?34 \d{9}"
result = re.findall(pattern, text)
print(result)

# {n}: Exactamente n veces
text = "aaaaaa"
pattern = "a{3}"
result = re.findall(pattern, text)
print(result)


# {n, m}: De n a m veces
text = "u uu uuu"
pattern = "u{2,3}"
result = re.findall(pattern, text)
print(result)

# Ejercicio 3:
# Encuentra las palabras de más de 4 a 6 letras
words = "ala casa árbol león cinco murcielago"
pattern = r"\b\w{4,6}\b"
result = re.findall(pattern, words) 
print(result)

# Ejercicio 4:
# Encuentra las palabras de más de 6 letras
words = "ala fantastico árbol león cinco murcielago"
pattern = r"\b\w{7,}\b"
result = re.findall(pattern, words)
print(result)