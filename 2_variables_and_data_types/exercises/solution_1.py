# ============================================
# Ejercicio 1: Información Personal
# ============================================
# Dificultad: Fácil
# Objetivo: Practicar creación de variables con diferentes tipos de datos
# Requisitos de código limpio: nombres descriptivos en snake_case
#
# TODO:
# 1. Crea variables para almacenar tu información personal:
#    - Nombre completo (string)
#    - Edad (int)
#    - Altura en metros (float)
#    - Si estás empleado actualmente (bool)
#    - Tu ciudad actual (string)
# 2. Imprime cada variable con un mensaje descriptivo
#    Ejemplo: "Mi nombre es: Ana García"
# 3. Usa f-strings para formatear la salida

name = "Carlos Andres Posada Chica"
age = 33
height_in_meters = 1.77
is_currently_employed = True
current_city = "Carepa"

print(f"Personal Information:\n"
      f"  name: {name}\n"
      f"  age: {age}\n"
      f"  height in meters: {height_in_meters}m \n"
      f"  is currently employed: {is_currently_employed}\n"
      f"  current city: {current_city}")