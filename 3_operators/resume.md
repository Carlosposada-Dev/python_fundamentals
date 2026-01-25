# Section 3: Operators - Summary

## 🎯 Key Concepts

- **Operators**: Symbols that tell Python what operations to perform on variables and values
- **7 operator types**: Arithmetic, Comparison, Logical, Assignment, Identity, Membership, Bitwise
- **Operator precedence**: Order in which Python evaluates operations (similar to math)
- **Short-circuit evaluation**: `and` and `or` optimize by not evaluating unnecessary expressions
- **Division types**: `/` (true division, returns float) vs `//` (floor division, returns int)
- **Modulo operator `%`**: Returns the remainder of division (useful for parity, cycles, distribution)

## 🎨 Best Practices and Conventions

### PEP 8 Applied to Operators

```python
# ✅ Correct spacing - one space before and after operators
x = 5 + 3
result = (a * b) + c
is_valid = age >= 18

# ❌ Incorrect - no spaces or inconsistent
x=5+3
result = (a*b)+c
is_valid = age>=18

# Exception: No spaces in default parameter values
def calculate_cost(instances=1, price_per_hour=0.10):
    pass
```

### Clean Code Applied

**Use parentheses for clarity:**
```python
# ❌ Confusing
result = a + b * c / d - e

# ✅ Clear
result = a + ((b * c) / d) - e
```

**Descriptive names for boolean results:**
```python
# ❌ Bad
x = cpu > 80

# ✅ Good
cpu_exceeded = cpu > 80
needs_alert = cpu > 80 and memory > 90
server_available = status == "running" and health_check_ok
```

**Avoid redundant comparisons with booleans:**
```python
# ❌ Redundant
if server_active == True:
    pass

# ✅ Direct
if server_active:
    pass

# ❌ Redundant
if server_active == False:
    pass

# ✅ Direct
if not server_active:
    pass
```

### Good vs Bad Code Examples

**❌ Bad example:**
```python
c = i / h * 730
if c > 100 and m > 80 or d > 90:
    a = True
```

**✅ Good example:**
```python
HOURS_PER_MONTH = 730
monthly_cost = instances * hourly_rate * HOURS_PER_MONTH

cpu_high = cpu_usage > 80
memory_high = memory_usage > 80
disk_high = disk_usage > 90

needs_attention = (cpu_high and memory_high) or disk_high
```

## 💡 Important Points to Remember

- **Division `/` always returns float** even with whole numbers: `10 / 2 = 5.0`
- **Floor division `//` truncates decimals**, doesn't round: `10 // 3 = 3`
- **Modulo `%` gives remainder**: Useful for parity checks, round-robin distribution, cycles
- **Operator precedence**: `**` > `*,/,//,%` > `+,-` > comparisons > `not` > `and` > `or`
- **Use parentheses when in doubt** - clarity over cleverness
- **Spacing matters for readability** - follow PEP 8 consistently
- **Short-circuit evaluation**: `False and expensive_function()` won't call the function

## ⚠️ Common Errors to Avoid

### Functional Errors

```python
# ❌ Confusing = (assignment) with == (comparison)
if x = 5:  # SyntaxError
    pass

# ✅ Correct
if x == 5:
    pass

# ❌ Division by zero
result = 10 / 0  # ZeroDivisionError

# ✅ Validate first
if divisor != 0:
    result = dividend / divisor

# ❌ Using / when you need //
servers = 1000 / 100  # 10.0 (float) - wrong for counting

# ✅ Correct
servers = 1000 // 100  # 10 (int)
```

### Style Errors

```python
# ❌ No spacing
x=5+3

# ❌ Inconsistent spacing
result = a*b + c

# ❌ Missing parentheses in complex expressions
calc = cpu * 100 / total + overhead

# ❌ Using tabs for alignment
print(f"Cost: \t\t${cost}")  # PEP 8 discourages tabs

# ✅ Use spaces or format differently
print(f"Cost: ${cost:.2f}")
```

## 🔗 Connection with Other Concepts

Operators work with **variables and data types** from the previous section:
- Arithmetic operators with `int` and `float`
- Comparison operators with any type
- Logical operators with `bool`
- Assignment operators with all types

You'll use operators extensively in:
- **Conditionals** (next): Making decisions with comparisons and logic
- **Loops**: Control flow with comparisons and counters
- **Functions**: Calculations and validations
- **Data structures**: Filtering and transforming data

## ✅ Mastery Checklist

- [x] Use arithmetic operators (+, -, *, /, //, %, **)
- [x] Understand the difference between / and //
- [x] Use comparison operators correctly
- [x] Combine conditions with and, or, not
- [x] Apply assignment operators (+=, -=, etc.)
- [x] Understand operator precedence
- [x] Use parentheses for clarity
- [x] Follow PEP 8 for operator spacing
- [x] Apply operators in DevOps/Cloud contexts

---

## 🎓 Complete Example with Best Practices

```python
"""
Server Resource Monitor
Analyzes metrics and determines scaling needs
"""

# Constants - Thresholds
CPU_WARNING = 70
CPU_CRITICAL = 90
MEMORY_WARNING = 80
MEMORY_CRITICAL = 95
MIN_INSTANCES = 2
MAX_INSTANCES = 10
REQUESTS_PER_INSTANCE_LIMIT = 1000

# Current metrics
cpu_usage = 85
memory_usage = 78
active_instances = 3
total_requests = 3500

# Calculations
cpu_available = 100 - cpu_usage
memory_available = 100 - memory_usage
requests_per_instance = total_requests // active_instances

# Health evaluations
cpu_in_warning = cpu_usage >= CPU_WARNING
cpu_in_critical = cpu_usage >= CPU_CRITICAL
memory_in_warning = memory_usage >= MEMORY_WARNING

# Complex conditions with parentheses for clarity
resources_healthy = (cpu_usage < CPU_CRITICAL) and (memory_usage < MEMORY_CRITICAL)
needs_attention = cpu_in_warning or memory_in_warning
overloaded = (requests_per_instance > REQUESTS_PER_INSTANCE_LIMIT) or cpu_in_critical

# Scaling decisions
can_scale_up = active_instances < MAX_INSTANCES
can_scale_down = active_instances > MIN_INSTANCES
should_scale_up = overloaded and can_scale_up
should_scale_down = (not needs_attention) and can_scale_down

# Assignment operators for counters
total_health_checks = 100
total_health_checks += 1  # More readable than total_health_checks = total_health_checks + 1

# Output
print("=== Server Health Report ===")
print(f"CPU Usage: {cpu_usage}% (Available: {cpu_available}%)")
print(f"Memory Usage: {memory_usage}% (Available: {memory_available}%)")
print(f"Requests/Instance: {requests_per_instance}")
print(f"\nHealth Status: {'Healthy' if resources_healthy else 'Degraded'}")
print(f"Needs Attention: {'Yes' if needs_attention else 'No'}")
print(f"Scaling Recommendation: {'Scale Up' if should_scale_up else 'Scale Down' if should_scale_down else 'Maintain'}")
```

**What makes this code clean:**
- Descriptive constant names in UPPER_SNAKE_CASE
- Clear variable names that reveal intent
- Proper spacing around all operators (PEP 8)
- Parentheses for clarity in complex conditions
- Boolean variables with descriptive names
- Logical flow from metrics → calculations → evaluations → decisions
- Comments explain sections, not obvious code

---

**Congratulations!** 🎉 You've completed Section 3 with excellent code quality. You now have solid foundations in Python operators with best practices applied from the start.