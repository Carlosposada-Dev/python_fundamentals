"""
## Exercise 5: Health Check Aggregator

**Difficulty**: Intermediate  
**Objective**: Practice multiple logical operators (and, or, not)  
**Context**: Determine if a server is completely healthy

### TODO:

1. Define constants for thresholds:
   - `CPU_MAX`: 85
   - `MEMORY_MAX`: 90
   - `DISK_MAX`: 80
   - `LATENCY_MAX_MS`: 200

2. Request from user the current metrics:
   - CPU usage (%)
   - Memory usage (%)
   - Disk usage (%)
   - Latency (ms)
   - Backup completed? (True/False - use input and convert)

3. Evaluate conditions:
   - `resources_ok`: CPU, memory and disk below threshold (use and)
   - `network_ok`: latency below threshold
   - `server_healthy`: resources_ok AND network_ok AND backup_completed
   - `requires_immediate_attention`: CPU > 95 OR memory > 95

4. Print results of all evaluations

### Note:
- This simulates an aggregated health check of multiple metrics

Write your solution in `solution_5.py`
"""

CPU_MAX = 85
MEMORY_MAX = 90
DISK_MAX = 80
LATENCY_MAX_MS = 200

print("\nMONITORING - HEALTH CHECK AGREGATOR\n")

cpu_usage = float(input("Please, enter the current CPU usage (%): "))
memory_usage = float(input("Please, enter the current memory usage (%): "))
disk_usage = float(input("Please, enter the current disk usage (%): "))
latency = float(input("Please, enter the current latency (ms): "))
backup_completed = input("Has backup completed? (yes/no): ").lower()
backup_completed = True if backup_completed == 'yes' else False

resource_ok = (cpu_usage < CPU_MAX) and (memory_usage < MEMORY_MAX) and (disk_usage < DISK_MAX)
network_ok = latency < LATENCY_MAX_MS
server_healthy = resource_ok and network_ok and backup_completed
requires_immediate_attention = (cpu_usage > 95) or (memory_usage > 95)

print(f"\nRESULTS:\n")
print(f"network_ok: {"Yes" if network_ok else "No"}")
print(f"resource_ok: {"Yes" if resource_ok else "No"}")
print(f"server_healthy: {"Yes" if server_healthy else "No"}")
print(f"requires_immediate_attention: {"Yes" if requires_immediate_attention else "No"}")
