"""
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
"""

MIN_INSTANCES = 2
MAX_INSTANCES = 10
CPU_SCALE_UP = 75
CPU_SCALE_DOWN = 30
REQUESTS_PER_INSTANCE = 1000
recommendation = ""

print("\nAuto-Scaling Decision Engine\n")

number_of_instances = int(input("Enter the number of active instances: "))
average_cpu = float(input("Enter the average CPU usage (%): "))
total_current_requests = int(input("Enter the total current requests: "))

requests_per_instance = total_current_requests // number_of_instances
need_scaled_up = (requests_per_instance > 1000) or (average_cpu > CPU_SCALE_UP)
need_scale_down = (requests_per_instance < 500) and (average_cpu < CPU_SCALE_DOWN) and (number_of_instances > MIN_INSTANCES)
at_max_limit = number_of_instances >= MAX_INSTANCES
at_min_limit = number_of_instances <= MIN_INSTANCES

if need_scaled_up and not at_max_limit:
    recommendation = " Scale Up"
elif  need_scale_down and not at_min_limit:
    recommendation = " Scale Down"
elif at_max_limit or at_min_limit:
    recommendation = "At limit"
else:
    recommendation = "Maintain"

print("\nAnalysis:\n")
print(f"- Instances: {number_of_instances}")
print(f"- CPU Usage: {average_cpu}%")
print(f"- Requests per Instance: {requests_per_instance}")
print(f"- Need Scale Up: {"Yes" if need_scaled_up else "No"}")
print(f"- Can Scale Down: {"Yes" if need_scale_down else "No"}")
print(f"- At Max Limit: {"Yes" if at_max_limit else "No"}")
print(f"- At Min Limit: {"Yes" if at_min_limit else "No"}")
print(f"- Recommendation: {recommendation}")