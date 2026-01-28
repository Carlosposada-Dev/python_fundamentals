"""
Exercise 1: Log Parser - Extract Information
Difficulty: Easy
Objective: Practice string slicing and basic methods

Context: Parse a log entry to extract key information.

Task:
1. Given this log entry:
   log = "2024-01-15 14:30:45 ERROR web-server-01 Connection timeout after 30s"

2. Extract and print:
   - Date (first 10 characters)
   - Time (characters 11-19)
   - Log level (ERROR, WARNING, INFO, etc.)
   - Server name
   - Error message

3. Use string slicing and split() method
4. Format output nicely with f-strings

Expected output:
   Date: 2024-01-15
   Time: 14:30:45
   Level: ERROR
   Server: web-server-01
   Message: Connection timeout after 30s
"""

# Your solution here