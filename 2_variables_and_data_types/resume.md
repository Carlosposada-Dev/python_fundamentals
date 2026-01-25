# Section 2: Variables & Data Types - Summary

## 🎯 Key Concepts

- **Variable**: Name that points to a value in memory
- **Dynamic Typing**: You don't need to declare types, Python infers them automatically
- **5 Basic Types**: `int`, `float`, `str`, `bool`, `None`
- **Type Conversion**: `int()`, `float()`, `str()` to convert between types
- **Type Checking**: `type()` shows the type of a variable

## 🎨 Best Practices and Conventions

### PEP 8 applied to variables

```python
# Variables and functions: snake_case
user_age = 25
height_meters = 1.77
full_name = "Carlos"

# Constants: UPPER_SNAKE_CASE
MAX_ATTEMPTS = 3
PI = 3.14159
MINIMUM_AGE = 18

# Correct spacing
x = 5  # ✅ One space before and after =
x=5    # ❌ No spaces
```

### Clean Code applied

**Descriptive names:**
```python
# ❌ Bad
x = 25
n = "Juan"
d = 1.75

# ✅ Good
user_age = 25
full_name = "Juan"
height_meters = 1.75
```

**Avoid magic numbers:**
```python
# ❌ Bad
if age < 18:
    print("Not allowed")

# ✅ Good
MINIMUM_AGE = 18
if age < MINIMUM_AGE:
    print("Not allowed")
```

## 💡 Important Points to Remember

- **One variable, one purpose**: Don't reuse variables for different things
- **Language consistency**: Choose English or Spanish, don't mix them
- **F-strings for formatting**: `f"Age: {age}"` is more readable
- **Input validation**: Always convert and validate data from the user
- **Specific try-except**: Catch specific errors, don't use bare `except:`

## ⚠️ Common Errors to Avoid

### Functional
```python
# ❌ Variable not defined
print(name)  # NameError

# ❌ Mixing incompatible types
age = "25"
result = age + 5  # TypeError

# ❌ Wrong try-except
except:
    variable: None  # ':' doesn't assign, use '='
```

### Style
```python
# ❌ Non-descriptive names
x = 25  # What is x?

# ❌ Not using constants
if attempts > 3:  # Why 3?

# ❌ Inconsistency
user_edad = 25  # Mixing English/Spanish
```

## 🔗 Connection with Other Concepts

- **Operators** (next): You'll manipulate variables with +, -, *, /, %, etc.
- **Strings**: Advanced methods for working with text
- **Conditionals**: You'll use booleans to make decisions
- **Loops**: You'll iterate over ranges using control variables
- **Functions**: Variables as parameters and return values

## 📝 Technical Vocabulary

- **Variable**: Name that references a value in memory
- **Data Type**: Classification that determines what operations are valid
- **Casting**: Conversion between types (`int()`, `float()`, `str()`)
- **Dynamic Typing**: The type is determined at runtime
- **Constant**: Variable whose value shouldn't change (convention)
- **snake_case**: Naming convention with underscores
- **Magic Number**: Hardcoded value without context

## ✅ Mastery Checklist

- [x] I create variables with different data types
- [x] I understand what dynamic typing is
- [x] I use `type()` to verify types
- [x] I convert between types correctly
- [x] I name variables in snake_case
- [x] I use constants in UPPER_SNAKE_CASE
- [x] I avoid magic numbers
- [x] I write code with descriptive names
- [x] I handle errors with specific try-except
