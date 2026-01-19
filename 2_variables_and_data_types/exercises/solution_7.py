# ============================================
# Ejercicio 7: Detector de Tipos de Datos
# ============================================
# Dificultad: Medio-Difícil
# Objetivo: Practicar conversión de tipos y uso de type()
# Requisitos de código limpio: manejo de errores, código robusto
#
# TODO:
# 1. Solicita al usuario que ingrese un valor
# 2. Intenta convertir el valor a diferentes tipos y muestra cuál funciona:
#    - Intenta convertir a int (si falla, captura el error)
#    - Intenta convertir a float (si falla, captura el error)
#    - Siempre se puede mantener como string
# 3. Imprime el tipo original del input (siempre es string)
# 4. Imprime qué conversiones fueron exitosas
# 5. Sugiere el "mejor tipo" para ese valor
#
# Ejemplos de comportamiento:
#   Input: "42" → Puede ser int, float o string. Mejor tipo: int
#   Input: "3.14" → Puede ser float o string. Mejor tipo: float
#   Input: "Hola" → Solo puede ser string. Mejor tipo: string
#
# PISTA: Usa try/except para manejar errores de conversión
# EXTRA: Este ejercicio te prepara para validación de entrada de usuario
#
# Escribe tu solución en soluciones.py

value = input("Please enter something: ")

try:
    int_value = int(value)
    can_be_int = True
except ValueError:
    int_value = None
    can_be_int = False
try:
    float_value = float(value)
    can_be_float = True
except ValueError:
    float_value = None
    can_be_float = False

print(f"\nOriginal type: {type(value).__name__}")

print(f"Successful conversions:")
if can_be_int:
    print("- int")
if can_be_float:
    print("- float")
print("- str (always possible)")

print("\nBest type suggestion:")
if can_be_int:
    print("- int")
elif can_be_float:
    print("- float")
else:
    print("- str")