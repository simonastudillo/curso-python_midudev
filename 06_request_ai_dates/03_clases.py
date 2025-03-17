# 1. Introducción a las clases
# Las clases son plantillas para crear objetos. Un objeto es una instancia de una clase.
# Nos permite agrupar datos y funciones que operan sobre esos datos.

# Ejemplo básico de una clase
class Coche:
  # atributo de clase (Compartido por todas las instancias)
  tipo = "coche"

  # método especial que es en que construye el objeto
  # se llama automaticamente al crear un objeto
  def __init__ (self, marca, modelo, color):
    # atributos de instancia
    self.marca = marca
    self.modelo = modelo
    self.color = color

  def arrancar(self):
    print(f"Arrancando el {self.marca} {self.modelo}")


# Encapsulación: es ocultar los detalles internos de una clase y exponer solo la interfaz pública.
