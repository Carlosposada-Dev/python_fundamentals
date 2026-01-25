# ============================================
# Exercise 7: Data Type Detector
# ============================================
# Difficulty: Intermediate-Advanced
# Objective: Practice type conversion and use of type()
# Clean Code Requirements: Error handling, robust code
#
# TODO:
# 1. Request a value from the user
# 2. Try converting the value to different types and show which work:
#    - Try converting to int (if it fails, catch the error)
#    - Try converting to float (if it fails, catch the error)
#    - Can always be kept as string
# 3. Print the original input type (always string)
# 4. Print which conversions were successful
# 5. Suggest the "best type" for that value
#
# Examples of behavior:
#   Input: "42" → Can be int, float or string. Best type: int
#   Input: "3.14" → Can be float or string. Best type: float
#   Input: "Hello" → Only can be string. Best type: string
#
# TIP: Use try/except to handle conversion errors
# EXTRA: This exercise prepares you for user input validation
#
# Write your solution in soluciones.py

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