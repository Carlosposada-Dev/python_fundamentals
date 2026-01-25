# ============================================
# Exercise 6: Tip Calculator
# ============================================
# Difficulty: Intermediate
# Objective: Work with multiple variables, constants, and calculations
# Clean Code Requirements: Constants for percentages, descriptive names
#
# TODO:
# 1. Define constants for tip percentages:
#    - Excellent service: 20% (0.20)
#    - Good service: 15% (0.15)
#    - Regular service: 10% (0.10)
# 2. Request from the user:
#    - The total bill amount
#    - The service level (1=regular, 2=good, 3=excellent)
# 3. Calculate the tip based on the service level
# 4. Calculate the total to pay (bill + tip)
# 5. Print:
#    - Bill amount
#    - Applied tip percentage
#    - Tip amount
#    - Total to pay
#
# NOTE: Use if/elif/else to determine the percentage based on the level
#
# Write your solution in soluciones.py

EXCELLENT_SERVICE_TIP = 0.20
GOOD_SERVICE_TIP = 0.15
REGULAR_SERVICE_TIP = 0.10

print("TIP CALCULATOR\n")
bill_amount = float(input("Please enter the total bill amount: "))
service_level = int(input("Please enter the service level (1 = regular, 2 = good, 3 = excellent): "))

if service_level == 3:
    tip_percentage = EXCELLENT_SERVICE_TIP
elif service_level == 2:
    tip_percentage = GOOD_SERVICE_TIP
elif service_level == 1:
    tip_percentage = REGULAR_SERVICE_TIP
else:
    print("Invalid service level. Please enter 1, 2, or 3.")
    exit()

tip_amount = bill_amount * tip_percentage
total_amount = bill_amount + tip_amount

print(f"Billing data:")
print(f" - Bill amount: ${bill_amount:.2f}")
print(f" - Tip percentage applied: {tip_percentage:.0%}")
print(f" - Tip amount: {tip_amount:.2f}")
print(f" - Total amount to pay: ${total_amount:.2f}")