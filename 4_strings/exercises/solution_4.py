"""
Exercise 4: Config File Key-Value Parser
Difficulty: Medium
Objective: Practice split(), strip(), and string manipulation

Context: Parse configuration strings in INI-like format.

Task:
1. Given a configuration string:
   config = "server=192.168.1.100 ; port=8080 ; ssl=true ; timeout=30"

2. Parse the config by:
   - Split by ';' to get individual settings
   - For each setting, split by '=' to get key and value
   - Strip whitespace from keys and values

3. Store in variables or print each setting:
   Server: 192.168.1.100
   Port: 8080
   SSL: true
   Timeout: 30

4. Convert the port to integer
5. Convert ssl string to boolean (True if "true", False if "false")

EXTRA: Handle case where user provides config with different spacing
"""

# Your solution here
