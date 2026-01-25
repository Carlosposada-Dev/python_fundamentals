# ============================================
# Exercise 5: Variable Swap
# ============================================
# Difficulty: Intermediate
# Objective: Practice multiple assignment and variable manipulation
# Clean Code Requirements: Descriptive names, show before/after clearly
#
# TODO:
# 1. Create two variables with different values:
#    - first_variable = 100
#    - second_variable = 200
# 2. Print the original values with a clear message
# 3. Swap the values of the variables using Python's multiple assignment
#    (without using a temporary variable)
# 4. Print the values after the swap
#
# Expected output:
#   Before: first = 100, second = 200
#   After: first = 200, second = 100
#
# Write your solution in soluciones.py

first_variable = 100
second_variable = 200

print(f"Before: first_variable = {first_variable}, second_variable = {second_variable}")

first_variable, second_variable = second_variable, first_variable

print(f"After: first_variable = {first_variable}, second_variable = {second_variable}")