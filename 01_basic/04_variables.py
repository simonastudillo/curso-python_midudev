###
# 04 - Variables
# Las variables sirven para guardar datos en memoria
# Python es un lenguaje de tipado dinamico y de tipado fuerte
###

# Asignar una variable solo hace falta poner esto
my_name = "Simon"
print(my_name)

age = 32
print(age)

age = 39
print(age)

# Tipado dinámico: el tipo de dato se determina en tiempo de ejecución
name = "Simon"
print("variable name es de tipo: " + str(type(name)))

name = 10
print("variable name es de tipo: " + str(type(name)))

# Tipado fuerte: Python no realiza conversiones de tipo automáticamente
# f-string (literal de cadena de formato) / desde la versión 3.6 de Python
print(f"hola {my_name}, tengo {age} años")

# Forma no recomendada de asignar variables
name, age, city = "Simon", 32, "Madrid"
print(name, age, city)

# Convensones de nombres de variables
mi_nombre_de_variable = "Simon"


is_user_logged_in: bool = True
print(is_user_logged_in)
is_user_logged_in = 42
print(is_user_logged_in)