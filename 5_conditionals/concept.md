# Section 5: Conditional Statements (if, elif, else)

## 🎯 What are Conditional Statements?

**Conditional statements** allow your program to make decisions and execute different code based on conditions. They're the foundation of program logic - enabling your code to respond differently to different situations.

In DevOps/Cloud, conditionals power everything: deployment decisions, health checks, alert routing, environment configurations, automated remediation, and infrastructure scaling logic.

You've already been using conditionals in previous exercises! Now we'll formalize that knowledge and explore advanced patterns.

## 🔀 Basic Conditional Structure

### if Statement

Executes code only if a condition is True.

```python
cpu_usage = 85

if cpu_usage > 80:
    print("⚠️  High CPU usage detected")
    send_alert = True
```

### if-else Statement

Executes one block if True, another if False.

```python
environment = "prod"

if environment == "prod":
    enable_debug = False
    log_level = "ERROR"
else:
    enable_debug = True
    log_level = "DEBUG"
```

### if-elif-else Statement

Tests multiple conditions in order (only the first True block executes).

```python
cpu_usage = 85

if cpu_usage >= 90:
    alert_level = "CRITICAL"
    action = "Scale immediately"
elif cpu_usage >= 70:
    alert_level = "WARNING"
    action = "Monitor closely"
else:
    alert_level = "NORMAL"
    action = "No action needed"
```

**Important:** Once a condition is True, Python executes that block and skips the rest (even if other conditions are also True).

## 🎯 Comparison Operators in Conditionals

```python
# Equality
if status == "running":
    pass

# Inequality
if port != 22:
    pass

# Greater than / Less than
if cpu > 80:
    pass
if memory < 1024:
    pass

# Greater or equal / Less or equal
if instances >= 3:
    pass
if response_time <= 200:
    pass

# Chained comparisons (Pythonic!)
if 0 <= port <= 65535:
    print("Valid port range")

# Membership
if "ERROR" in log_message:
    pass
if environment not in ["dev", "staging"]:
    pass
```

## 🔗 Logical Operators in Conditionals

### and - All conditions must be True

```python
cpu_ok = cpu_usage < 80
memory_ok = memory_usage < 90

if cpu_ok and memory_ok:
    print("✅ Server healthy")

# More complex
if cpu_usage < 80 and memory_usage < 90 and disk_usage < 85:
    server_status = "healthy"
```

### or - At least one condition must be True

```python
if status == "stopped" or status == "terminated":
    print("Instance not running")

# Alert on any critical resource
if cpu_usage > 95 or memory_usage > 95 or disk_usage > 95:
    trigger_alert("CRITICAL")
```

### not - Inverts the boolean value

```python
if not backup_completed:
    print("⚠️  Backup pending")

if not server_available:
    initiate_failover()
```

### Combining Logical Operators

Use parentheses for clarity!

```python
# Complex health check
if (cpu_usage < 80 and memory_usage < 90) or is_maintenance_mode:
    allow_traffic = True

# Deployment validation
if environment == "prod" and (tests_passed and approval_received):
    deploy()
```

## 💡 Truthiness and Falsiness

In Python, values are evaluated as True or False in boolean context (beyond just `True` and `False`).

### Falsy Values (evaluate to False)

```python
# These all evaluate to False in conditionals:
- False
- None
- 0, 0.0
- "" (empty string)
- [] (empty list)
- {} (empty dict)
- () (empty tuple)

# Examples:
server_name = ""
if server_name:  # False - empty string
    print("Server configured")

error_count = 0
if error_count:  # False - zero
    print("Errors detected")

config = None
if config:  # False - None
    print("Config loaded")
```

### Truthy Values (evaluate to True)

```python
# Everything else is Truthy:
- True
- Any non-zero number (1, -1, 3.14)
- Any non-empty string ("hello", "0", "False")
- Any non-empty collection ([1], {"a": 1})

# Examples:
server_name = "web-01"
if server_name:  # True - non-empty string
    print(f"Configuring {server_name}")

error_count = 5
if error_count:  # True - non-zero
    print(f"Found {error_count} errors")
```

### Practical Use

```python
# Instead of explicit comparison
if len(servers) > 0:  # Verbose
    pass

# Use truthiness (Pythonic)
if servers:  # Clean - empty list is False
    pass

# Instead of checking None explicitly
if config is not None:  # Verbose
    pass

# Use truthiness
if config:  # Clean - None is False
    pass
```

## 🔄 Ternary Operator (Conditional Expression)

A compact way to assign values based on a condition.

### Syntax

```python
value_if_true if condition else value_if_false
```

### Examples

```python
# Traditional if-else
if environment == "prod":
    log_level = "ERROR"
else:
    log_level = "DEBUG"

# Ternary operator (more concise)
log_level = "ERROR" if environment == "prod" else "DEBUG"

# More examples
status = "✅ Active" if is_running else "❌ Stopped"
port = 443 if use_ssl else 80
max_instances = 10 if environment == "prod" else 3
```

**When to use:**
- ✅ Simple value assignments based on condition
- ✅ When it improves readability
- ❌ Avoid for complex logic (use regular if-else)
- ❌ Don't nest ternaries (hard to read)

## 🏗️ Nested Conditionals

Conditionals inside other conditionals.

```python
# Nested conditionals
if environment == "prod":
    if cpu_usage > 90:
        scale_up()
    elif cpu_usage < 30:
        scale_down()
    else:
        maintain()
else:
    # Dev/staging - no auto-scaling
    print("Auto-scaling disabled in non-prod")
```

**Warning:** Too many levels create "arrow code" (hard to read). Use guard clauses instead.

## 🛡️ Guard Clauses (Early Returns)

Handle edge cases first, reducing nesting.

```python
# ❌ Bad - deeply nested
def deploy_application(environment, tests_passed, approved):
    if environment == "prod":
        if tests_passed:
            if approved:
                print("Deploying to production")
                # deployment logic here
            else:
                print("Approval required")
        else:
            print("Tests must pass")
    else:
        print("Not production environment")

# ✅ Good - guard clauses (early returns)
def deploy_application(environment, tests_passed, approved):
    if environment != "prod":
        print("Not production environment")
        return
    
    if not tests_passed:
        print("Tests must pass")
        return
    
    if not approved:
        print("Approval required")
        return
    
    # Happy path - clear and not nested
    print("Deploying to production")
    # deployment logic here
```

## 🎨 Best Practices with Conditionals

### ✅ Use Parentheses for Complex Conditions

```python
# ❌ Confusing
if cpu > 80 and memory > 90 or disk > 95 and errors > 10:
    pass

# ✅ Clear with parentheses
if (cpu > 80 and memory > 90) or (disk > 95 and errors > 10):
    pass
```

### ✅ Avoid Redundant Comparisons with Booleans

```python
# ❌ Redundant
if is_running == True:
    pass
if server_active == False:
    pass

# ✅ Direct
if is_running:
    pass
if not server_active:
    pass
```

### ✅ Use Chained Comparisons

```python
# ❌ Verbose
if value >= 0 and value <= 100:
    pass

# ✅ Pythonic
if 0 <= value <= 100:
    pass

# ❌ Verbose
if port > 1024 and port < 65535:
    pass

# ✅ Pythonic
if 1024 < port < 65535:
    pass
```

### ✅ Use 'in' for Multiple Values

```python
# ❌ Repetitive
if status == "stopped" or status == "terminated" or status == "stopping":
    pass

# ✅ Clean
if status in ["stopped", "terminated", "stopping"]:
    pass

# Works with any iterable
PROD_ENVIRONMENTS = ["production", "prod", "prd"]
if environment in PROD_ENVIRONMENTS:
    pass
```

### ✅ Consistent Comparison Order

```python
# ✅ Variable on left, constant on right (natural reading)
if cpu_usage > CPU_THRESHOLD:
    pass

if environment == "prod":
    pass

# Also valid: Yoda conditions (prevents accidental assignment in some languages)
# Not necessary in Python (if x = 5 is a syntax error)
if "prod" == environment:  # Less common in Python
    pass
```

### ✅ Use Descriptive Boolean Variable Names

```python
# ❌ Unclear
if x:
    pass

# ✅ Clear intent
if server_is_healthy:
    pass
if deployment_approved:
    pass
if tests_passed:
    pass
```

## ⚠️ Common Errors

### 1. Using Assignment (=) Instead of Comparison (==)

```python
# ❌ Syntax Error
if environment = "prod":  # SyntaxError
    pass

# ✅ Correct
if environment == "prod":
    pass
```

### 2. Missing Colon (:)

```python
# ❌ Syntax Error
if cpu > 80  # SyntaxError: missing colon
    print("High CPU")

# ✅ Correct
if cpu > 80:
    print("High CPU")
```

### 3. Incorrect Indentation

```python
# ❌ IndentationError
if cpu > 80:
print("High CPU")  # Must be indented

# ✅ Correct
if cpu > 80:
    print("High CPU")
```

### 4. Confusing 'and' with 'or'

```python
# ❌ Wrong logic - will never trigger
if cpu > 95 or memory > 95:  # Triggers if EITHER is high
    alert("Resource critical")

# If you meant "both must be high":
if cpu > 95 and memory > 95:
    alert("Both resources critical")
```

### 5. Not Using 'elif' When Needed

```python
# ❌ All conditions evaluated (inefficient, possible bugs)
if score >= 90:
    grade = "A"
if score >= 80:  # Still checked even if score is 95
    grade = "B"  # Overwrites "A"!
if score >= 70:
    grade = "C"

# ✅ Correct - only first match executes
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

### 6. Confusing Truthiness

```python
# ❌ Unexpected behavior
servers = []
if servers:  # False - empty list
    print("Have servers")  # Won't print

# ✅ Be explicit when needed
if len(servers) > 0:  # Clear intent
    print("Have servers")

# But truthiness is fine for None checks
config = None
if not config:  # Pythonic
    load_config()
```

## 💡 Advanced Patterns

### Multiple Conditions for Same Action

```python
# ❌ Repetitive
if status == "stopped":
    restart_instance()
if status == "terminated":
    restart_instance()
if status == "error":
    restart_instance()

# ✅ Use 'in' or 'or'
if status in ["stopped", "terminated", "error"]:
    restart_instance()
```

### Default Values with Conditionals

```python
# Using ternary for defaults
port = user_port if user_port else 8080
environment = env_var if env_var else "development"

# Or using 'or' with truthiness
port = user_port or 8080
environment = env_var or "development"
```

### Conditional with Multiple Actions

```python
# Good structure for multiple related actions
if environment == "prod":
    log_level = "ERROR"
    enable_monitoring = True
    backup_frequency = "hourly"
    max_instances = 10
elif environment == "staging":
    log_level = "WARNING"
    enable_monitoring = True
    backup_frequency = "daily"
    max_instances = 5
else:  # dev
    log_level = "DEBUG"
    enable_monitoring = False
    backup_frequency = "weekly"
    max_instances = 2
```

## 🔗 Connection with Previous Concepts

Conditionals use **comparison operators** from Section 3:
- `==`, `!=`, `>`, `<`, `>=`, `<=`
- `and`, `or`, `not`

Conditionals test **strings** from Section 4:
- `if "ERROR" in log:`
- `if environment.lower() == "prod":`
- `if server_name.startswith("web-"):`

Conditionals evaluate **variables** from Section 2:
- Testing values, types, truthiness

## ✅ Checklist of Mastery

- [ ] Use if, elif, else correctly
- [ ] Combine conditions with and, or, not
- [ ] Understand truthiness and falsiness
- [ ] Use chained comparisons (0 <= x <= 100)
- [ ] Apply ternary operator for simple cases
- [ ] Use guard clauses to reduce nesting
- [ ] Use 'in' for multiple value checks
- [ ] Avoid common mistakes (= vs ==, indentation)
- [ ] Write clear, readable conditionals with good naming
- [ ] Apply conditionals in DevOps decision-making

---

**Now it's your turn!** 🎤

Before moving to exercises, please answer these questions in your own words:

1. **What's the difference between `if/elif/else` and multiple separate `if` statements? When would you use each?**

2. **Explain truthiness and falsiness. Give 3 examples of falsy values and explain why this concept is useful.**

3. **What are guard clauses and why are they better than deeply nested conditionals?**

4. **When should you use a ternary operator vs a regular if-else statement?**