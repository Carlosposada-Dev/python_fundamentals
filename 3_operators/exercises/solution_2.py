"""
## Exercise 2: CPU Monitor - Alert System

**Difficulty**: Beginner-Intermediate  
**Objective**: Practice comparison and logical operators  
**Context**: Determine alert level based on CPU usage

### TODO:

1. Define constants for thresholds:
   - `CPU_WARNING`: 70%
   - `CPU_CRITICAL`: 90%

2. Request from the user the current CPU usage percentage
3. Calculate available CPU percentage
4. Determine status using comparison operators:
   - `normal_state`: CPU < 70%
   - `warning_state`: CPU >= 70% and < 90%
   - `critical_state`: CPU >= 90%

5. Print:
   - CPU usage and available CPU
   - Current status (Normal, Warning, or Critical)

### Tip:
- Use logical operators (and) for ranges
"""

CPU_WARNING = 70.0
CPU_CRITICAL = 90.0

print("CPU MONITOR - ALERT SYSTEM\n")
current_cpu_usage = float(input("Please, enter the current cpu usage percentage: "))

available_cpu_percentage = 100 - current_cpu_usage
current_cpu_usage_status = ""

normal_state = current_cpu_usage < CPU_WARNING
warning_state = (current_cpu_usage >= CPU_WARNING) and (current_cpu_usage < CPU_CRITICAL)
critical_state = current_cpu_usage >= CPU_CRITICAL

if critical_state:
    current_cpu_usage_status = "Critical"
elif warning_state:
    current_cpu_usage_status = "Warning"
else:
    current_cpu_usage_status = "Normal"

print("\nCPU USAGE REPORT:")
print(f"- Current CPU usage is: {current_cpu_usage:.2f}%")
print(f"- Available CPU percentage is: {available_cpu_percentage:.2f}%")
print(f"- Current CPU status is: {current_cpu_usage_status}")