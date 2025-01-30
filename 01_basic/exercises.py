###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en clase
###

# Ejercicio 1
print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y ciudad en lineas separadas")
# Tu solución
print("Simón");
print("Madrid");

# Ejercicio 2
print("\nEjercicio 2: Muestra los tipos de datos de las siguentes variables")
print("Usa el comando type() para determinar el tipo de datos de cada variable");
a = 15
b = 3.14159
c = "Hola Mundo"
d = True
e = None

# Tu solución
print(f"a: {type(a)}")
print(f"b: {type(b)}")
print(f"c: {type(c)}")
print(f"d: {type(d)}")
print(f"e: {type(e)}")

# Ejercicio 3
print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float")
print("Convierte el float 3.99 a un entero. ¿Que ocurre?")

# Tu solución
a = "12345"
a = int(a)
print(f"a: {a}")
a = float(a)
print(f"a: {a}")
b = 3.99
b = int(b)
print(f"b: {b}. Al transformar un flaot a int solo quita los decimales, no hace un round")

# Ejercicio 4
print("\nEjercicio 4: Variables")
print("Crea una variable llamada nombre, edad y altura")
print("usa f-strings para imprmir una presentación")

# Tu solución
nombre = "Simón"
edad = 32
altura = 1.80
print(f"Mi nombre es {nombre}, tengo {edad} años y {altura} metros de altura")

# Ejercicio 5
print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz a división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

# Tu solución
print( int(round(3.14159) / 2) )