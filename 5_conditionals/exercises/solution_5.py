"""
Exercise 5: IP Address Validator (Basic)
Difficulty: Medium
Objective: Practice split(), isdigit(), and validation logic

Context: Validate if a string is a valid IPv4 address (basic check).

Task:
1. Ask user for an IP address
2. Validate that it's a valid IPv4 format:
   - Must have exactly 4 octets separated by dots
   - Each octet must be a number
   - Each octet must be between 0-255

3. Use split('.') to break into parts
4. Check each part:
   - Is it a digit? (use isdigit())
   - Is it in valid range?

5. Print whether IP is valid or not
6. If invalid, explain why (e.g., "Invalid: octet 256 is out of range")

Test cases:
   - "192.168.1.1" → Valid
   - "192.168.1.256" → Invalid (256 > 255)
   - "192.168.1" → Invalid (only 3 octets)
   - "192.168.1.abc" → Invalid (abc is not a number)
"""

# The solution it's developing only with the concepts that have been seen until this point.

print("\nIP Address Validator\n")\

ip_address = input("Enter an IPv4 address (e.g., 192.168.10.15): ")

if ip_address.count(".") != 3:
    print("Invalid IP: Must contain exactly 4 octects separated by dots.")
    exit()

ip_address = ip_address.strip()
octect_1, octect_2, octect_3, octect_4 = ip_address.split(".")

if not octect_1.isdigit() or int(octect_1) > 255:
   print(f"Invalid IP: Octect 1 {octect_1} is not a valid number between 0-255.")
   exit()
elif not octect_2.isdigit() or int(octect_2) > 255:
   print(f"Invalid IP: Octect 2 {octect_2} is not a valid number between 0-255.")
   exit()
elif not octect_3.isdigit() or int(octect_3) > 255:
   print(f"Invalid IP: Octect 3 {octect_3} is not a valid number between 0-255.")
   exit()
elif not octect_4.isdigit() or int(octect_4) > 255:
   print(f"Invalid IP: Octect 4 {octect_4} is not a valid number between 0-255.")
   exit()
else:
   print(f"Valid IP Address: {ip_address}")
   