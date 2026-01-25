"""
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

"""

print("\nIP parity checker and pool assignment\n")
last_octet = int(input("Enter the last octet of the IP (0-255): "))
full_ip = f"192.168.1.{last_octet}"
is_even = last_octet % 2 == 0
is_multiple_of_5 = last_octet % 5 == 0
is_multiple_of_10 =  last_octet % 10 == 0

if is_even:
    parity = "Even"
    assigned_pool = "Pool A (web servers)"
else:
    parity = "Odd"
    assigned_pool = "Pool B (application servers)"

print(f"\nComplete IP: {full_ip}")
print(f"Parity: {parity}")
print(f"Assigned Pool: {assigned_pool}")
print(f"Multiple of 5: {"Yes" if is_multiple_of_5 else "No"}")
print(f"Multiple of 10: {"Yes" if is_multiple_of_10 else "No"}")