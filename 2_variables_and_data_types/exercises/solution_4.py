# ============================================
# Exercise 4: Age Validation
# ============================================
# Difficulty: Intermediate
# Objective: Work with constants, booleans, and data validation
# Clean Code Requirements: Constants in UPPER_CASE, descriptive boolean names
#
# TODO:
# 1. Define constants for:
#    - Minimum age to vote (18)
#    - Minimum age to get a driver's license (16)
#    - Age of adulthood (18)
# 2. Request the user's age
# 3. Create boolean variables to determine if the person:
#    - Can vote
#    - Can drive
#    - Is an adult
# 4. Print results with clear messages
#    Example: "Can you vote? True" or "Can you vote? False"
#
# EXTRA: Boolean variable names should be self-descriptive
# Suggestion: can_vote, can_drive, is_adult
#
# Write your solution in soluciones.py

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