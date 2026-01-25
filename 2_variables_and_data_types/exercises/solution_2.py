# ============================================
# Exercise 2: Rectangle Area Calculator
# ============================================
# Difficulty: Beginner
# Objective: Work with math operations and type conversion
# Clean Code Requirements: Avoid magic numbers, descriptive names
#
# TODO:
# 1. Request from the user the width of the rectangle (can have decimals)
# 2. Request from the user the height of the rectangle (can have decimals)
# 3. Calculate the area of the rectangle
# 4. Calculate the perimeter of the rectangle
# 5. Print results with 2 decimal precision
#
# EXTRA: Make sure to convert inputs to float
# NOTE: Area = width × height, Perimeter = 2 × (width + height)
#
# Write your solution in solution_2.py

width = float(input("Please, enter the rectangle widht in cm(can be decimal): "))
height = float(input ("Please, enter the rectangle height in cm(can be decimal): "))

area =  width * height
perimeter = 2 * (width + height)

print (f"Rectangle area is : {area:.2f} cm²")
print (f"Rectangle perimeter is: {perimeter:.2f} cm")