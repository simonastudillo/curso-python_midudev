###
# 04 - Dictionaries
# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos relacionados.
###

# ejemplo tipico de diccionario
persona = {
  "nombre": "midudev",
  "edad": 25,
  "es_estudiante": True,
  "calificaciones": [7, 8, 9],
  "socials": {
    "twitter": "@midudev",
    "instagram": "@midudev",
    "facebook": "midudev"
  }
}

# para acceder a un valor
print(persona["nombre"])
print(persona["calificaciones"][2])
print(persona["socials"]["twitter"])

# para modificar un valor
persona["nombre"] = "midu"
persona["calificaciones"][2] = 10
persona["socials"]["twitter"] = "@midu"

# para borrar un valor
del persona["socials"]

es_estudiante = persona.pop("es_estudiante")
print(f"es_estudiante = {es_estudiante}")

print(persona)


a = {"name": "midu", "age": 25}
b = {"name": "simon", "es_estudiante": True}

a.update(b)
print(a)

print("name" in persona) # False
print("nombre" in persona) # True

print(persona.keys()) # Obtener las claves
print(persona.values()) # Obtener los valores
print(persona.items()) # Obtener las claves y los valores

for key, value in persona.items():
  print(f"{key} = {value}")