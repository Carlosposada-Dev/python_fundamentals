# ============================================
# Exercise 3: Temperature Converter
# ============================================
# Difficulty: Beginner-Intermediate
# Objective: Practice type conversion and use of constants
# Clean Code Requirements: Use constants for formulas, avoid magic numbers
#
# TODO:
# 1. Define constants for conversion formulas:
#    - Multiplication factor Celsius to Fahrenheit (9/5)
#    - Adjustment value for Fahrenheit (32)
# 2. Request a temperature in Celsius from the user
# 3. Convert to Fahrenheit using: F = C × (9/5) + 32
# 4. Convert to Kelvin using: K = C + 273.15
# 5. Print all three temperatures with clear messages
#
# EXTRA: Format outputs with 2 decimal places
#
# Write your solution in soluciones.py

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
ADJUST_VALUE_FAHRENHEIT = 32
KELVIN_CONSTANT = 273.15

celsius_temperature = float(input("Please, enter the temperature in celsisus degree: "))
fahrenheit_temperature = (celsius_temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + ADJUST_VALUE_FAHRENHEIT
kelvin_temperature = celsius_temperature + KELVIN_CONSTANT

print(f"Temperature in Celsius degree: {celsius_temperature:.2f} °C")
print(f"Temperature in Fahrenheit degree: {fahrenheit_temperature:.2f} °F")
print(f"Temperature in Kelvin: {kelvin_temperature:.2f} K")