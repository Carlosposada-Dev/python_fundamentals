# ============================================
# Ejercicio 5: Intercambio de Variables (Swap)
# ============================================
# Dificultad: Medio
# Objetivo: Practicar asignación múltiple y manipulación de variables
# Requisitos de código limpio: nombres descriptivos, demostrar antes/después claramente
#
# TODO:
# 1. Crea dos variables con valores diferentes:
#    - primera_variable = 100
#    - segunda_variable = 200
# 2. Imprime los valores originales con un mensaje claro
# 3. Intercambia los valores de las variables usando asignación múltiple de Python
#    (sin usar una variable temporal)
# 4. Imprime los valores después del intercambio
#
# Salida esperada:
#   Antes: primera = 100, segunda = 200
#   Después: primera = 200, segunda = 100
#
# Escribe tu solución en soluciones.py

first_variable = 100
second_variable = 200

print(f"Before: first_variable = {first_variable}, second_variable = {second_variable}")

first_variable, second_variable = second_variable, first_variable

print(f"After: first_variable = {first_variable}, second_variable = {second_variable}")