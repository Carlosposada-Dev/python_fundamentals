# Section 2: Variables & Data Types

## 🎯 What Are Variables?

A **variable** is a container that stores data in your computer's memory. Think of it as a labeled box where you keep information that you'll need to use later.

In Python, creating a variable is as simple as giving it a name and assigning it a value:

```python
age = 25
name = "Ana"
temperature = 36.5
is_active = True
```

### Important Characteristics of Variables in Python:

1. **Dynamic Typing**: You don't need to declare the data type explicitly. Python infers it automatically.
2. **Reassignable**: You can change the value (and even the type) of a variable whenever you want.
3. **Case-sensitive**: `age`, `Age` and `AGE` are three different variables.

## 📊 Basic Data Types in Python

Python has several fundamental data types. Here are the most important ones to get started:

### 1. **Integers (int)** - Numbers without decimals

```python
user_age = 25
current_year = 2025
temperature_celsius = -5
```

### 2. **Floats (float)** - Numbers with decimals

```python
height_meters = 1.75
product_price = 49.99
pi = 3.14159
```

### 3. **Strings (str)** - Text in quotes

```python
full_name = "María García"
city = 'Bogotá'
message = """This is a text
that spans multiple lines"""
```

**Note**: You can use single `' '` or double `" "` quotes, but the convention is to use double quotes for regular strings.

### 4. **Booleans (bool)** - Truth values

```python
is_logged_in = True
is_adult = False
has_discount = True
```

**Important**: `True` and `False` start with a capital letter in Python.

### 5. **NoneType** - Absence of value

```python
result = None  # No value assigned yet
current_user = None  # No logged-in user
```

## 🔍 Checking the Type of a Variable

Use the `type()` function to find out what data type a variable is:

```python
age = 30
print(type(age))  # <class 'int'>

price = 99.99
print(type(price))  # <class 'float'>

name = "Python"
print(type(name))  # <class 'str'>
```

## 🔄 Type Conversion (Type Casting)

Sometimes you need to convert one data type to another:

```python
# String to integer
age_text = "25"
age_number = int(age_text)  # 25 (int)

# Integer to string
points = 100
message = "You have " + str(points) + " points"

# String to float
price_text = "49.99"
price_number = float(price_text)  # 49.99 (float)

# Float to int (loses decimals)
average = 8.7
average_int = int(average)  # 8 (truncates, doesn't round)
```

## 🎨 Good Practices with Variables

### ✅ Descriptive Names (PEP 8)

Variable names should reveal their intention. Anyone reading your code should understand what the variable contains without needing comments.

**❌ Bad:**
```python
x = 25
n = "Juan"
d = 1.75
t = True
p = 49.99
```

**✅ Good:**
```python
user_age = 25
full_name = "Juan"
height_meters = 1.75
is_active = True
product_price = 49.99
```

### ✅ Python Naming Convention (snake_case)

Python uses **snake_case** for variables and functions: words in lowercase separated by underscores.

```python
# Normal variables: snake_case
full_name = "Ana López"
current_age = 30
total_products = 5
average_temperature = 22.5

# Constants: UPPER_SNAKE_CASE
PI = 3.14159
MAX_ATTEMPTS = 3
MINIMUM_AGE = 18
BASE_URL = "https://api.example.com"

# Single-word names: no underscores
age = 25
name = "Pedro"
price = 99.99
```

### ✅ Avoid Magic Numbers

A "magic number" is a hardcoded value without context. Use constants with descriptive names.

**❌ Bad:**
```python
if age < 18:
    print("You cannot register")

final_price = price * 0.19
```

**✅ Good:**
```python
MINIMUM_REGISTRATION_AGE = 18
if age < MINIMUM_REGISTRATION_AGE:
    print("You cannot register")

TAX_RATE = 0.19
final_price = price * TAX_RATE
```

### ✅ One Variable, One Purpose

Avoid reusing variables for different purposes. Create a new variable with a descriptive name.

**❌ Bad:**
```python
data = input("Name: ")
print(f"Hello {data}")
data = int(input("Age: "))  # Reusing 'data' for something else
print(f"You are {data} years old")
```

**✅ Good:**
```python
name = input("Name: ")
print(f"Hello {name}")
age = int(input("Age: "))
print(f"You are {age} years old")
```

### ✅ English vs Spanish Names

**Recommendation**: Choose a language and maintain consistency throughout your project.

- **English**: Industry standard, facilitates international collaboration
- **Spanish**: Valid for local or educational projects

```python
# Option 1: All in English
user_age = 25
product_price = 49.99

# Option 2: All in Spanish
edad_usuario = 25
precio_producto = 49.99

# ❌ DON'T MIX
user_edad = 25  # Inconsistent
precio_product = 49.99  # Inconsistent
```

## 💡 Important Concepts

### Multiple Assignment

Python allows you to assign values to multiple variables in one line:

```python
# Assign different values
name, age, city = "Ana", 28, "Medellín"

# Assign the same value
x = y = z = 0

# Swap values
a = 5
b = 10
a, b = b, a  # Now a=10, b=5
```

### Variables and Memory

When you assign a value to a variable, Python creates an object in memory and the variable is just a "label" that points to that object.

```python
age = 25  # Python creates an int object with value 25
age = 30  # Python creates a NEW int object with value 30
```

### Reserved Words

Python has words that you CANNOT use as variable names because they have special meanings:

```python
# ❌ DON'T USE AS VARIABLES:
# False, True, None, and, or, not, if, else, elif, 
# for, while, break, continue, def, class, return, etc.

# This causes an error:
for = 10  # SyntaxError
class = "Python"  # SyntaxError
```

## 🎓 Comparison with Other Languages

If you come from other languages, here are some key differences:

| Aspect | Java/C++ | Python |
|--------|----------|--------|
| Declaration | `int age = 25;` | `age = 25` |
| Typing | Static | Dynamic |
| Semicolon | Required `;` | Not used |
| Constants | `final int MAX = 10;` | `MAX = 10` (convention) |

## ⚠️ Common Errors

### 1. Undefined variables
```python
print(name)  # NameError: name 'name' is not defined
# First you must assign: name = "Ana"
```

### 2. Mixing incompatible types
```python
age = "25"
result = age + 5  # TypeError: can't concatenate str and int
# Solution: result = int(age) + 5
```

### 3. Invalid names
```python
1age = 25  # SyntaxError: cannot start with a number
my-variable = 10  # SyntaxError: hyphen is interpreted as subtraction
my variable = 5  # SyntaxError: spaces not allowed
```

### 4. Confusing assignment (=) with comparison (==)
```python
age = 25  # Assignment: you give the value 25 to age
age == 25  # Comparison: you ask if age equals 25 (returns True/False)
```

## 📝 Complete Example with Good Practices

```python
"""
Program: BMI Calculator (Body Mass Index)
Demonstrates correct use of variables and data types
"""

# Constants (values that don't change)
BMI_UNDERWEIGHT = 18.5
BMI_NORMAL_WEIGHT = 24.9
BMI_OVERWEIGHT = 29.9

# User data input
patient_name = input("Enter your name: ")
weight_kilograms = float(input("Enter your weight in kg: "))
height_meters = float(input("Enter your height in meters: "))

# BMI calculation
body_mass_index = weight_kilograms / (height_meters ** 2)

# Category determination
if body_mass_index < BMI_UNDERWEIGHT:
    category = "Underweight"
elif body_mass_index <= BMI_NORMAL_WEIGHT:
    category = "Normal weight"
elif body_mass_index <= BMI_OVERWEIGHT:
    category = "Overweight"
else:
    category = "Obesity"

# Display results
print(f"\n--- Results for {patient_name} ---")
print(f"BMI: {body_mass_index:.2f}")
print(f"Category: {category}")
```

**Notice what makes this code clean:**
- Descriptive names that reveal intention
- Constants for important values
- Consistent snake_case
- Comments that explain sections, not the obvious
- Clear and readable calculations

## 🔗 Connection with What's Next

Variables and data types are the foundation of EVERYTHING in programming. In the next sections you'll see:

- **Operators**: How to manipulate and combine variables
- **Strings**: Advanced methods for working with text
- **Data Structures**: Lists, dictionaries to group variables
- **Functions**: How to organize your code using variables as parameters

## ✅ Mastery Checklist

Before continuing, make sure you can:

- [ ] Create variables with different data types
- [ ] Explain what dynamic typing is
- [ ] Use `type()` to verify data types
- [ ] Convert between types (int, float, str)
- [ ] Name variables following snake_case
- [ ] Identify and avoid magic numbers
- [ ] Write code with descriptive names

---

**Now it's your turn!** 🎤

Before moving on to the exercises, I need to validate that you've understood these concepts.

Please answer these questions in your own words:

1. **What is a variable and why is it important to use descriptive names?**
2. **What is the difference between `int`, `float` and `str`? Give me an example of when you would use each one.**
3. **What does it mean that Python has "dynamic typing"? How does it differ from Java or C++?**
4. **What is a "magic number" and why should we avoid them?**

Take your time to think and answer. There's no rush, what matters is that you understand these fundamentals well. 😊