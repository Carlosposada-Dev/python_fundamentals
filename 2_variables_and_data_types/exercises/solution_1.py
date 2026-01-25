# ============================================
# Exercise 1: Personal Information
# ============================================
# Difficulty: Beginner
# Objective: Practice creating variables with different data types
# Clean Code Requirements: Descriptive names in snake_case
#
# TODO:
# 1. Create variables to store your personal information:
#    - Full name (string)
#    - Age (int)
#    - Height in meters (float)
#    - Currently employed (bool)
#    - Your current city (string)
# 2. Print each variable with a descriptive message
#    Example: "My name is: Ana García"
# 3. Use f-strings to format the output

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