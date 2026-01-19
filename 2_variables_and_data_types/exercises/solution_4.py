# ============================================
# Ejercicio 4: Validación de Edad
# ============================================
# Dificultad: Medio
# Objetivo: Trabajar con constantes, booleanos y validación de datos
# Requisitos de código limpio: constantes en UPPER_CASE, nombres booleanos descriptivos
#
# TODO:
# 1. Define constantes para:
#    - Edad mínima para votar (18)
#    - Edad mínima para licencia de conducir (16)
#    - Edad para ser mayor de edad (18)
# 2. Solicita al usuario su edad
# 3. Crea variables booleanas que determinen si la persona:
#    - Puede votar
#    - Puede conducir
#    - Es mayor de edad
# 4. Imprime el resultado de cada validación con mensajes claros
#    Ejemplo: "¿Puedes votar? True" o "¿Puedes votar? False"
#
# EXTRA: Los nombres de variables booleanas deben ser autodescriptivos
# Sugerencia: puede_votar, puede_conducir, es_mayor_edad
#
# Escribe tu solución en soluciones.py

AGE_MIN_VOTE = 18
AGE_MIN_DRIVE_LICENSE = 16
AGE_OF_ADULTHOOD = 18

user_age = int(input("Please enter your age: "))
if user_age < 0:
    print("Age cannot be negative")

can_vote = user_age >= AGE_MIN_VOTE
can_drive = user_age >= AGE_MIN_DRIVE_LICENSE
is_adult = user_age >= AGE_OF_ADULTHOOD

print(f"Can you vote: {can_vote}")
print(f"Can you drive: {can_drive}")
print(f"Are you an adult: {is_adult}")