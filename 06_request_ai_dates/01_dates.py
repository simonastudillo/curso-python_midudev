# Trabajando con fechas y horas en Python

from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_TIME, 'es_ES')

# 1. Obtener la fecha y hora actual
now = datetime.now()
print(f"fecha y hora actual: {now}");

# 2. Crear una fecha específica
specific_date = datetime(2020, 12, 25)
print(f"fecha y hora: {specific_date}");

# 3. Formatear fechas
# método strftime() para formatear fechas
# pasarle el objeto datetime y el formato especificado (https://strftime.org/)

# Formato: dd/mm/YY H:M:S

formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")
print(f"fecha y hora formateada: {formatted_date}");
formatted_date = now.strftime("%d/%m/%y %H:%M:%S")
print(f"fecha y hora formateada: {formatted_date}");

formatted_date = now.strftime("%A")
print(f"fecha y hora formateada: {formatted_date}");

# 4. Operaciones con fechas (sumar y restar días, horas minutos, meses)

yesterday = now - timedelta(days=1)
print(f"ayer: {yesterday}");

tomorrow = now + timedelta(days=1)
print(f"mañana: {tomorrow}");

oneHourAfter = now + timedelta(hours=1)
print(f"una hora después: {oneHourAfter}");

# 5. Obtener los componentes de una fecha

print(f"Año: {now.year}");
print(f"Mes: {now.month}");
print(f"Día: {now.day}");

# 6. Calcular la diferencia entre dos fechas

date1 = datetime(2020, 12, 25)
date2 = datetime(2021, 1, 1)
difference = date2 - date1;
print(f"diferencia: {difference}");