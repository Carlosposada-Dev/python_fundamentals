# Section 4: Strings

## 🎯 What are Strings?

A **string** (str) is a sequence of characters used to represent text in Python. Strings are immutable, meaning once created, they cannot be modified - any operation that appears to modify a string actually creates a new one.

In DevOps/Cloud, you'll work with strings constantly: parsing logs, building commands, formatting outputs, processing configuration files, constructing API requests, and manipulating file paths.

```python
# Creating strings
server_name = "web-server-01"
log_message = 'Connection established'
multiline = """This is a
multi-line string
for documentation"""

# Strings are immutable
text = "hello"
text[0] = "H"  # TypeError: 'str' object does not support item assignment
```

## 📝 String Creation and Quotes

### Single vs Double Quotes

Both are valid - choose one and be consistent. PEP 8 doesn't mandate one over the other.

```python
# Single quotes
server = 'production-db-01'

# Double quotes (preferred for strings containing apostrophes)
message = "Server's status is OK"

# Triple quotes for multi-line strings
documentation = """
Server Configuration:
- Name: web-01
- Region: us-east-1
- Status: running
"""
```

### Raw Strings (r-strings)

Useful for regex patterns, file paths (especially Windows), and strings with backslashes.

```python
# Regular string (backslash must be escaped)
windows_path = "C:\\Users\\Admin\\logs\\app.log"

# Raw string (backslashes treated literally)
windows_path = r"C:\Users\Admin\logs\app.log"

# Regex patterns
pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"  # IP address pattern
```

## 🔤 String Indexing and Slicing

Strings are sequences - you can access individual characters or substrings.

### Indexing

```python
server = "web-server-01"

# Positive indexing (starts at 0)
server[0]   # 'w'
server[4]   # 's'

# Negative indexing (starts at -1 from the end)
server[-1]  # '1'
server[-2]  # '0'
server[-3]  # '-'
```

### Slicing

Syntax: `string[start:end:step]` (end is exclusive)

```python
log = "2024-01-15 10:30:45 ERROR Connection timeout"

# Basic slicing
log[0:10]    # '2024-01-15' (year-month-day)
log[11:19]   # '10:30:45' (time)
log[20:25]   # 'ERROR'

# Omitting start/end
log[:10]     # '2024-01-15' (from beginning)
log[20:]     # 'ERROR Connection timeout' (to end)

# Negative indices
log[-7:]     # 'timeout'
log[:-8]     # '2024-01-15 10:30:45 ERROR Connection'

# Step (every nth character)
log[::2]     # '20401510045ERO onetmo'
log[::-1]    # Reverse: 'tuoemit noitcennoC RORRE 54:03:01 51-10-4202'
```

## 🔧 String Methods

Python strings have dozens of built-in methods. Here are the most important for DevOps/Cloud work:

### Case Conversion

```python
server_name = "Web-Server-01"

server_name.upper()      # 'WEB-SERVER-01'
server_name.lower()      # 'web-server-01'
server_name.capitalize() # 'Web-server-01'
server_name.title()      # 'Web-Server-01'
server_name.swapcase()   # 'wEB-sERVER-01'
```

**Use case:** Normalizing hostnames, comparing case-insensitive values

```python
# Case-insensitive comparison
env = input("Environment (dev/staging/prod): ")
if env.lower() == "prod":
    print("⚠️  Production environment - proceed with caution")
```

### Trimming Whitespace

```python
log_line = "   ERROR: Disk full   \n"

log_line.strip()   # 'ERROR: Disk full' (both ends)
log_line.lstrip()  # 'ERROR: Disk full   \n' (left only)
log_line.rstrip()  # '   ERROR: Disk full' (right only)
```

**Use case:** Cleaning user input, parsing logs

### Searching and Checking

```python
log = "Connection timeout after 30 seconds"

# Find substring
log.find("timeout")      # 11 (index where found)
log.find("success")      # -1 (not found)
log.index("timeout")     # 11 (raises ValueError if not found)

# Check if contains
"timeout" in log         # True
"success" in log         # False

# Check start/end
log.startswith("Connection")  # True
log.endswith("seconds")       # True

# Count occurrences
log.count("t")           # 4
```

**Use case:** Log analysis, filtering, validation

### Replacing

```python
config = "server=localhost;port=8080;ssl=false"

# Replace substring
config.replace("localhost", "192.168.1.100")
# 'server=192.168.1.100;port=8080;ssl=false'

config.replace("false", "true")
# 'server=localhost;port=8080;ssl=true'

# Replace with count limit
text = "test test test"
text.replace("test", "prod", 2)  # 'prod prod test' (only first 2)
```

**Use case:** Modifying configuration strings, templating

### Splitting and Joining

```python
# Split string into list
config = "web-01,web-02,web-03,db-01"
servers = config.split(",")  # ['web-01', 'web-02', 'web-03', 'db-01']

log = "2024-01-15 10:30:45 ERROR Connection timeout"
parts = log.split()  # Split by whitespace (default)
# ['2024-01-15', '10:30:45', 'ERROR', 'Connection', 'timeout']

# Split with limit
parts = log.split(" ", 2)  # ['2024-01-15', '10:30:45', 'ERROR Connection timeout']

# Join list into string
servers = ["web-01", "web-02", "web-03"]
",".join(servers)   # 'web-01,web-02,web-03'
" | ".join(servers) # 'web-01 | web-02 | web-03'
```

**Use case:** Parsing CSV data, constructing commands, building reports

### Type Checking

```python
# Check character types
"12345".isdigit()     # True
"abc123".isalpha()    # False
"abc123".isalnum()    # True
"   ".isspace()       # True
"Web-Server".istitle()  # True
"192.168.1.1".replace(".", "").isdigit()  # True (IP validation helper)
```

**Use case:** Input validation, parsing

## 🎨 String Formatting

### F-strings (Recommended - Python 3.6+)

The most modern and readable way to format strings.

```python
server = "web-01"
cpu = 85.7
memory = 4096

# Basic f-string
message = f"Server {server} is running"

# Expressions inside f-strings
status = f"CPU: {cpu}%, Memory: {memory}MB"

# Formatting numbers
price = 0.0416
f"${price:.2f}"        # '$0.04' (2 decimals)
f"${price:.4f}"        # '$0.0416' (4 decimals)

# Percentage
usage = 0.857
f"{usage:.1%}"         # '85.7%'

# Padding and alignment
f"{server:>15}"        # '         web-01' (right-align, 15 chars)
f"{server:<15}"        # 'web-01         ' (left-align)
f"{server:^15}"        # '    web-01     ' (center)
f"{cpu:06.2f}"         # '085.70' (pad with zeros)
```

**Use case:** Building log messages, formatting reports, constructing commands

### format() Method

Older but still valid approach.

```python
"Server {} has {}% CPU usage".format(server, cpu)
"Server {0} has {1}% CPU usage".format(server, cpu)
"Server {name} has {usage}% CPU usage".format(name=server, usage=cpu)
```

### %-formatting (Legacy - Avoid)

```python
# Old style - don't use in new code
"Server %s has %d%% CPU usage" % (server, cpu)
```

## 🔤 String Operators

```python
# Concatenation (+)
first = "web"
last = "server"
full = first + "-" + last  # 'web-server'

# Repetition (*)
separator = "=" * 40  # '========================================'
border = "-" * 20     # '--------------------'

# Membership (in)
"error" in log_message  # True or False
"ERROR" in log_message.upper()  # Case-insensitive check
```

## 🎨 Best Practices with Strings

### ✅ Use f-strings for Formatting

```python
# ❌ Bad - hard to read
message = "Server " + server_name + " has " + str(cpu_usage) + "% CPU"

# ❌ Bad - outdated
message = "Server %s has %d%% CPU" % (server_name, cpu_usage)

# ✅ Good - clear and modern
message = f"Server {server_name} has {cpu_usage}% CPU"
```

### ✅ Use Raw Strings for Paths and Regex

```python
# ❌ Bad - escaping nightmare
path = "C:\\Users\\Admin\\Documents\\logs\\app.log"
pattern = "\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}"

# ✅ Good - readable
path = r"C:\Users\Admin\Documents\logs\app.log"
pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
```

### ✅ Use Triple Quotes for Multi-line Strings

```python
# ❌ Bad - concatenation mess
help_text = "Usage: deploy.py [options]\n" + \
            "Options:\n" + \
            "  -e, --environment  Specify environment\n" + \
            "  -v, --verbose      Verbose output"

# ✅ Good - natural and readable
help_text = """
Usage: deploy.py [options]
Options:
  -e, --environment  Specify environment
  -v, --verbose      Verbose output
"""
```

### ✅ Use join() Instead of Concatenation in Loops

```python
servers = ["web-01", "web-02", "web-03", "db-01"]

# ❌ Bad - inefficient (creates new string each iteration)
result = ""
for server in servers:
    result = result + server + ", "

# ✅ Good - efficient
result = ", ".join(servers)
```

### ✅ Be Explicit with String Methods

```python
# ❌ Ambiguous
text = input().strip().lower()

# ✅ Clear intention
user_input = input()
normalized_input = user_input.strip().lower()
```

## 💡 Important Concepts

### String Immutability

```python
# Strings cannot be modified in place
server = "web-server-01"
server[0] = "W"  # TypeError

# You must create a new string
server = "W" + server[1:]  # "Web-server-01"
# OR use string methods
server = server.replace("w", "W", 1)
```

### Escape Sequences

```python
# Special characters
print("Line 1\nLine 2")       # \n = newline
print("Column1\tColumn2")     # \t = tab
print("He said \"Hello\"")    # \" = quote
print("Path: C:\\Windows")    # \\ = backslash

# Or use raw strings to avoid escaping
print(r"C:\Windows\System32")
```

### String Concatenation vs Formatting

```python
# Concatenation (only for simple cases)
greeting = "Hello, " + name

# Formatting (better for complex cases)
message = f"Server {name} on {ip}:{port} is {status}"
```

## ⚠️ Common Errors

### 1. Trying to Modify Strings Directly
```python
# ❌ Error
text = "hello"
text[0] = "H"  # TypeError

# ✅ Correct
text = "H" + text[1:]
# OR
text = text.capitalize()
```

### 2. Forgetting Strings are Zero-Indexed
```python
server = "web-01"
# ❌ Wrong - index 6 doesn't exist (0-5 are valid)
server[6]  # IndexError

# ✅ Correct
server[5]  # '1'
server[-1]  # '1' (last character)
```

### 3. Confusing find() and index()
```python
log = "Connection established"

# find() returns -1 if not found
log.find("error")  # -1 (safe)

# index() raises exception if not found
log.index("error")  # ValueError (crashes if not handled)

# ✅ Good practice
if "error" in log:
    position = log.index("error")
```

### 4. Not Stripping Input
```python
# ❌ Problem
user_input = input("Enter environment: ")  # User types "prod   \n"
if user_input == "prod":  # False! (has trailing spaces)
    pass

# ✅ Solution
user_input = input("Enter environment: ").strip()
if user_input == "prod":  # True
    pass
```

### 5. Inefficient String Concatenation
```python
# ❌ Bad - creates new string each iteration
result = ""
for i in range(1000):
    result += str(i)

# ✅ Good - much more efficient
result = "".join(str(i) for i in range(1000))
```

## 🔗 Connection with Previous Concepts

Strings work with **operators** from the previous section:
- Concatenation: `+`
- Repetition: `*`
- Comparison: `==`, `!=`, `<`, `>` (lexicographic order)
- Membership: `in`, `not in`

You'll use strings with **variables and types**:
- Converting to strings: `str()`
- Type checking: `isinstance(text, str)`

## ✅ Checklist of Mastery

- [ ] Create strings with different quote styles
- [ ] Access characters using indexing and slicing
- [ ] Use common string methods (upper, lower, strip, split, join)
- [ ] Format strings using f-strings
- [ ] Search and replace within strings
- [ ] Understand string immutability
- [ ] Use raw strings for paths and regex
- [ ] Follow PEP 8 for string formatting
- [ ] Apply string operations in DevOps contexts

---

**Now it's your turn!** 🎤

Before moving to exercises, please answer these questions in your own words:

1. **What does "strings are immutable" mean? Give an example of what you cannot do and how to work around it.**
2. **Explain the difference between `find()` and `index()`. When would you use each one?**
3. **What's the difference between `split()` and `join()`? Give an example of when you'd use each in DevOps.**
4. **Why are f-strings preferred over string concatenation with `+`? Give an example.**