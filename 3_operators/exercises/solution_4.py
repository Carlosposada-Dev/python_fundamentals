"""
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
"""

network_and_broadcast_ips = 2
max_subnet_mask = 32

print("\nSUBNET CALCULATOR - AVAILABLE HOSTS\n")

subnet_mask = int(input("Please, enter a enter number for the subnet mask (e.g, 24 for /24): "))
if subnet_mask < 1 or subnet_mask > 32:
    print("Invalid subnet mask. Must be between 1 and 32")
    
number_of_subnets = int(input("Please, enter the desired number of subnets to divide into: "))

total_ips = 2 ** (max_subnet_mask - subnet_mask)
usable_hosts = total_ips - network_and_broadcast_ips
host_per_subnet = usable_hosts // number_of_subnets

print(f"\nFor a /{subnet_mask} subnet mask:")
print(f"Total IP addresses: {total_ips}")
print(f"Usable hosts: {usable_hosts}")
print(f"For {number_of_subnets} subnets: {host_per_subnet} IPs per subnet")
