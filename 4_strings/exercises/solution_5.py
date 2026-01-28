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