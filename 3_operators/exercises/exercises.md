# Section 3: Operators - Practical Exercises

## 📋 General Instructions

- Follow PEP 8 conventions (correct spacing around operators)
- Use descriptive variable names in snake_case
- Define constants in UPPER_SNAKE_CASE
- Avoid magic numbers
- Use parentheses for clarity in complex expressions
- Create your `solucion_#.py` file with your answers

---

## Exercise 1: AWS EC2 Cost Calculator

**Difficulty**: Beginner  
**Objective**: Practice basic arithmetic operators  
**Context**: Calculate monthly cost of EC2 instances

### TODO:

1. Define constants:
   - Hours per month: 730
   - Cost per hour for t3.medium instance: $0.0416

2. Request from the user the number of instances to deploy
3. Calculate:
   - Monthly cost per instance
   - Total monthly cost (all instances)
   - Annual cost (12 months)

4. Print results with 2 decimal places
   - Suggested format: `"Cost per instance per month: $30.37"`

Write your solution in `solution_1.py`

---

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

Write your solution in `solution_2.py`

---

## Exercise 3: Round-Robin Load Balancer

**Difficulty**: Intermediate  
**Objective**: Practice modulo operator (%)  
**Context**: Distribute requests among servers using round-robin

### TODO:

1. Define constant:
   - `TOTAL_SERVERS`: 4

2. Simulate 15 incoming requests
3. For each request, calculate which server it should go to using modulo:
   ```python
   assigned_server = request_number % TOTAL_SERVERS
   ```

4. Print the distribution of the first 10 requests
   - Format: `"Request #1 → Server 1"`
   - `"Request #2 → Server 2"`
   - etc.

### Note:
- This simulates a simple load balancing algorithm

### Extra:
- Count how many requests go to each server

Write your solution in `solution_3.py`

---

## Exercise 4: Subnet Calculator - Available Hosts

**Difficulty**: Intermediate  
**Objective**: Practice power operator (**) and integer division (//)  
**Context**: Calculate available hosts in a subnet

### TODO:

1. Request from the user the subnet mask (example: 24 for /24)
2. Calculate:
   - Total IP addresses = 2 ** (32 - mask)
   - Usable hosts = total_addresses - 2 (network and broadcast)

3. If user wants to distribute hosts across multiple subnets:
   - Request desired number of subnets
   - Calculate hosts per subnet using integer division (//)

4. Print all results

### Example:
```
Mask: /24
Total IPs: 256
Usable hosts: 254
If divided into 2 subnets: 127 hosts per subnet
```

Write your solution in `solution_4.py`

---

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

---

## Exercise 6: Auto-Scaling Decision Engine

**Difficulty**: Intermediate-Advanced  
**Objective**: Combine all learned operators  
**Context**: Decide whether to scale instances based on multiple metrics

### TODO:

1. Define constants:
   - `MIN_INSTANCES`: 2
   - `MAX_INSTANCES`: 10
   - `CPU_SCALE_UP`: 75
   - `CPU_SCALE_DOWN`: 30
   - `REQUESTS_PER_INSTANCE`: 1000

2. Request current data:
   - Number of active instances
   - Average CPU (%)
   - Total current requests

3. Calculate:
   - Requests per instance = total_requests // instances
   - Need scale up? (CPU > 75 OR requests_per_instance > 1000)
   - Can scale down? (CPU < 30 AND requests_per_instance < 500 AND instances > MIN)
   - At max limit? (instances >= MAX)
   - At min limit? (instances <= MIN)

4. Determine recommended action:
   - `"Scale Up"` if needed and not at maximum
   - `"Scale Down"` if possible and not at minimum
   - `"Maintain"` if in equilibrium
   - `"At limit"` if can't scale more

5. Print complete analysis and recommendation

### Extra:
- Calculate how many instances to add/remove (±1 or ±2 based on severity)

Write your solution in `solution_6.py`

---

## Exercise 7: IP Address Parity Checker

**Difficulty**: Intermediate  
**Objective**: Practice modulo operator for parity verification  
**Context**: Classify IPs for different pools (even/odd)

### TODO:

1. Request from the user the last octet of an IP (0-255)
   - Example: For 192.168.1.100, enter 100

2. Verify:
   - Is it even or odd? (use modulo %)
   - Is it a multiple of 5? (useful for creating pools every 5 IPs)
   - Is it divisible by 10?

3. Based on parity, assign to a pool:
   - Even IPs → Pool A (web servers)
   - Odd IPs → Pool B (application servers)

4. Print:
   - Complete IP (assume 192.168.1.X network)
   - Parity (Even/Odd)
   - Assigned pool
   - If it's a multiple of 5 or 10

### Note:
- In real networks this is used for segmentation and organization

Write your solution in `solution_7.py`

---

## ✅ Important

1. Create a file called `solution_7.py` in the same folder
2. Test your code with different input values
3. Think about edge cases (0%, 100%, negative values, etc.)
4. Apply PEP 8 and Clean Code principles
5. When you finish, share your code for review

**Good luck! 🚀**