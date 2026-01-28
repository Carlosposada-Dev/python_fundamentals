"""
Exercise 6: Log Level Counter and Filter
Difficulty: Medium-Hard
Objective: Practice string searching, counting, and filtering

Context: Analyze multiple log entries.

Task:
1. Given these log entries (combine into one multi-line string):
   logs = '''
   2024-01-15 10:00:00 INFO Server started successfully
   2024-01-15 10:05:23 WARNING High memory usage detected
   2024-01-15 10:10:45 ERROR Database connection failed
   2024-01-15 10:15:12 INFO Request processed
   2024-01-15 10:20:33 ERROR Timeout connecting to API
   2024-01-15 10:25:01 WARNING Disk usage above 80%
   2024-01-15 10:30:00 INFO Backup completed
   '''

2. Split logs into individual lines (use splitlines() or split('\\n'))

3. Count occurrences of each log level:
   - INFO count
   - WARNING count
   - ERROR count

4. Filter and display only ERROR logs

5. Create a summary report with:
   - Total logs processed
   - Count by level
   - List of ERROR messages

EXTRA: Find which error occurred first (earliest timestamp)
"""

# Your solution here

