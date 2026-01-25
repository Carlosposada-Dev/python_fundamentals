# Section 2: Variables & Data Types - Exercises

## 📋 General Instructions

- Follow PEP 8 conventions (snake_case, descriptive names, proper spacing)
- Use variable names that reveal their intention
- Avoid magic numbers - use constants with descriptive names
- Comment your code only when necessary (code should be self-explanatory)
- Think about edge cases and validations
- Create a `soluciones.py` file with your answers
- **Keep consistency in language (English or Spanish) throughout all exercises**

---

## Exercise 1: Personal Information

**Difficulty**: Beginner  
**Objective**: Practice creating variables with different data types  
**Clean Code Requirements**: Descriptive names in snake_case

### TODO:

1. Create variables to store your personal information:
   - Full name (string)
   - Age (int)
   - Height in meters (float)
   - Currently employed (bool)
   - Current city (string)

2. Print each variable with a descriptive message
   - Example: `"My name is: Ana García"`

3. Use f-strings for formatting the output

Write your solution in `soluciones.py`

---

## Exercise 2: Rectangle Area Calculator

**Difficulty**: Beginner  
**Objective**: Work with math operations and type conversion  
**Clean Code Requirements**: Avoid magic numbers, descriptive names

### TODO:

1. Request from the user the width of the rectangle (can have decimals)
2. Request from the user the height of the rectangle (can have decimals)
3. Calculate the area of the rectangle
4. Calculate the perimeter of the rectangle
5. Print results with 2 decimal precision

### Extra:
- Ensure you convert inputs to float

### Note:
- Area = width × height
- Perimeter = 2 × (width + height)

Write your solution in `soluciones.py`

---

## Exercise 3: Temperature Converter

**Difficulty**: Beginner-Intermediate  
**Objective**: Practice type conversion and use of constants  
**Clean Code Requirements**: Use constants for formulas, avoid magic numbers

### TODO:

1. Define constants for conversion formulas:
   - Multiplication factor Celsius to Fahrenheit (9/5)
   - Adjustment value for Fahrenheit (32)

2. Request a temperature in Celsius from the user
3. Convert to Fahrenheit using: `F = C × (9/5) + 32`
4. Convert to Kelvin using: `K = C + 273.15`
5. Print all three temperatures with clear messages

### Extra:
- Format outputs with 2 decimal places

Write your solution in `soluciones.py`

---

## Exercise 4: Age Validation

**Difficulty**: Intermediate  
**Objective**: Work with constants, booleans, and data validation  
**Clean Code Requirements**: Constants in UPPER_CASE, descriptive boolean names

### TODO:

1. Define constants for:
   - Minimum age to vote (18)
   - Minimum age to drive (16)
   - Age of majority (18)

2. Request the user's age
3. Create boolean variables to determine if the person:
   - Can vote
   - Can drive
   - Is of legal age

4. Print results with clear messages
   - Example: `"Can you vote? True"` or `"Can you vote? False"`

### Extra:
- Boolean variable names should be self-descriptive
- Suggestion: `can_vote`, `can_drive`, `is_legal_age`

Write your solution in `soluciones.py`

---

## Exercise 5: Variable Swap

**Difficulty**: Intermediate  
**Objective**: Practice multiple assignment and variable manipulation  
**Clean Code Requirements**: Descriptive names, show before/after clearly

### TODO:

1. Create two variables with different values:
   ```python
   first_variable = 100
   second_variable = 200
   ```

2. Print the original values with a clear message
3. Swap values using Python's multiple assignment (without a temporary variable)
4. Print values after the swap

### Expected Output:
```
Before: first = 100, second = 200
After: first = 200, second = 100
```

Write your solution in `soluciones.py`

---

## Exercise 6: Tip Calculator

**Difficulty**: Intermediate  
**Objective**: Work with multiple variables, constants, and calculations  
**Clean Code Requirements**: Constants for percentages, descriptive names

### TODO:

1. Define constants for tip percentages:
   - Excellent service: 20% (0.20)
   - Good service: 15% (0.15)
   - Regular service: 10% (0.10)

2. Request from the user:
   - Total bill amount
   - Service level (1=regular, 2=good, 3=excellent)

3. Calculate the tip based on service level
4. Calculate total to pay (bill + tip)
5. Print:
   - Bill amount
   - Applied tip percentage
   - Tip amount
   - Total to pay

### Note:
- Use if/elif/else to determine percentage based on level

Write your solution in `soluciones.py`

---

## Exercise 7: Data Type Detector

**Difficulty**: Intermediate-Advanced  
**Objective**: Practice type conversion and use of `type()`  
**Clean Code Requirements**: Error handling, robust code

### TODO:

1. Request a value from the user
2. Try converting the value to different types and show which work:
   - Try converting to int (catch error if it fails)
   - Try converting to float (catch error if it fails)
   - Always can be kept as string

3. Print the original input type (always string)
4. Print which conversions were successful
5. Suggest the "best type" for that value

### Examples:
- Input: `"42"` → Can be int, float or string. Best type: int
- Input: `"3.14"` → Can be float or string. Best type: float
- Input: `"Hello"` → Only can be string. Best type: string

### Tip:
- Use try/except to handle conversion errors

### Extra:
- This exercise prepares you for user input validation

Write your solution in `soluciones.py`

---

## ✅ Important

1. Create a file called `soluciones.py` in the same folder
2. Copy the exercise number as a comment before each solution
3. Solve each exercise applying PEP 8 and Clean Code
4. When finished, share your complete code for review
5. Don't worry if something doesn't work perfectly, we're here to learn!

**¡Good luck! 🚀**