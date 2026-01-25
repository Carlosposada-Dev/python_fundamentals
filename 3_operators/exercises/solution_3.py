"""
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
"""

TOTAL_SERVERS = 4
requests_server_1 = 0
requests_server_2 = 0
requests_server_3 = 0
requests_server_4 = 0

# Loop and list concept are introduced later, so we limit to first 10 requests manually
print("ROUD-ROBIN LOAD BALANCER\n")

module_request_1 = 1 % TOTAL_SERVERS
module_request_2 = 2 % TOTAL_SERVERS
module_request_3 = 3 % TOTAL_SERVERS
module_request_4 = 4 % TOTAL_SERVERS
module_request_5 = 5 % TOTAL_SERVERS
module_request_6 = 6 % TOTAL_SERVERS
module_request_7 = 7 % TOTAL_SERVERS
module_request_8 = 8 % TOTAL_SERVERS
module_request_9 = 9 % TOTAL_SERVERS
module_request_10 = 10 % TOTAL_SERVERS

print(f"Request #1 \t → Server {module_request_1}")
print(f"Request #2 \t → Server {module_request_2}")
print(f"Request #3 \t → Server {module_request_3}")
print(f"Request #4 \t → Server {module_request_4 + 4}")
print(f"Request #5 \t → Server {module_request_5}")
print(f"Request #6 \t → Server {module_request_6}")
print(f"Request #7 \t → Server {module_request_7}")
print(f"Request #8 \t → Server {module_request_8 + 4}")
print(f"Request #9 \t → Server {module_request_9}")
print(f"Request #10 \t → Server {module_request_10}")

if module_request_1 == 1:
    requests_server_1 += 1
if module_request_2 == 2:
    requests_server_2 += 1
if module_request_3 == 3:
    requests_server_3 += 1
if module_request_4 == 0:
    requests_server_4 += 1
if module_request_5 == 1:
    requests_server_1 += 1
if module_request_6 == 2:
    requests_server_2 += 1
if module_request_7 == 3:
    requests_server_3 += 1
if module_request_8 == 0:
    requests_server_4 += 1
if module_request_9 == 1:
    requests_server_1 += 1
if module_request_10 == 2:
    requests_server_2 += 1

print("\nREQUESTS DISTRIBUTION:")
print(f"Server 1 received {requests_server_1} requests.")
print(f"Server 2 received {requests_server_2} requests.")
print(f"Server 3 received {requests_server_3} requests.")
print(f"Server 4 received {requests_server_4} requests.")