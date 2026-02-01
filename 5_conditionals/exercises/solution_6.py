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

# The solution it's developing only with the concepts that have been seen until this point.

print("\nLOG LEVEL COUNTER AND FILTER\n")

logs = '''
   2024-01-15 10:00:00 INFO Server started successfully
   2024-01-15 10:05:23 WARNING High memory usage detected
   2024-01-15 10:10:45 ERROR Database connection failed
   2024-01-15 10:15:12 INFO Request processed
   2024-01-15 10:20:33 ERROR Timeout connecting to API
   2024-01-15 10:25:01 WARNING Disk usage above 80%
   2024-01-15 10:30:00 INFO Backup completed
   '''
error_count = logs.count("ERROR")
warning_count = logs.count("WARNING")
info_count = logs.count("INFO")

log_strip = logs.strip()
total_logs = log_strip.count("\n") + 1

first_error_msg = ""
second_error_msg = ""

if error_count >= 1:
    first_error_idx = logs.find("ERROR")
    msg_start = first_error_idx + len("ERROR ")
    msg_end = logs.find("\n", msg_start)
    first_error_msg = logs[msg_start:msg_end].strip()
    
    line_start = logs.rfind("\n", 0, first_error_idx) + 1
    first_error_timestamp = logs[line_start:line_start + 19].strip()

if error_count >= 2:
    second_error_idx = logs.find("ERROR", first_error_idx + 1)
    msg_start = second_error_idx + len("ERROR ")
    msg_end = logs.find("\n", msg_start)
    second_error_msg = logs[msg_start:msg_end].strip()
    
    line_start = logs.rfind("\n", 0, second_error_idx) + 1
    second_error_timestamp = logs[line_start:line_start + 19].strip()

# Display summary
print("\nLOG ANALYSIS SUMMARY:\n")
print(f"Total logs processed: {total_logs}")
print(f"\nCount by level:")
print(f"  - INFO: {info_count}")
print(f"  - WARNING: {warning_count}")
print(f"  - ERROR: {error_count}")

if error_count > 0:
    print(f"\nERROR Messages:")
    print(f"  1. [{first_error_timestamp}] {first_error_msg}")
    if error_count >= 2:
        print(f"  2. [{second_error_timestamp}] {second_error_msg}")

