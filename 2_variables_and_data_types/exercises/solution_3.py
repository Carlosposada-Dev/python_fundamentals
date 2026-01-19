# ============================================
# Ejercicio 3: Conversor de Temperatura
# ============================================
# Dificultad: Fácil-Medio
# Objetivo: Practicar conversión de tipos y uso de constantes
# Requisitos de código limpio: usar constantes para fórmulas, evitar números mágicos
#
# TODO:
# 1. Define constantes para las fórmulas de conversión:
#    - Factor de multiplicación Celsius a Fahrenheit (9/5)
#    - Valor de ajuste para Fahrenheit (32)
# 2. Solicita al usuario una temperatura en Celsius
# 3. Convierte la temperatura a Fahrenheit usando: F = C × (9/5) + 32
# 4. Convierte la temperatura a Kelvin usando: K = C + 273.15
# 5. Imprime las tres temperaturas con mensajes claros
#
# EXTRA: Formatea las salidas con 2 decimales
#
# Escribe tu solución en soluciones.py

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
ADJUST_VALUE_FAHRENHEIT = 32
KELVIN_CONSTANT = 273.15

celsius_temperature = float(input("Please, enter the temperature in celsisus degree: "))
fahrenheit_temperature = (celsius_temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + ADJUST_VALUE_FAHRENHEIT
kelvin_temperature = celsius_temperature + KELVIN_CONSTANT

print(f"Temperature in Celsius degree: {celsius_temperature:.2f} °C")
print(f"Temperature in Fahrenheit degree: {fahrenheit_temperature:.2f} °F")
print(f"Temperature in Kelvin: {kelvin_temperature:.2f} K")