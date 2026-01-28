"""
Exercise 3: Server Hostname Generator
Difficulty: Medium
Objective: Practice string formatting, concatenation, and methods

Context: Generate standardized server hostnames.

Task:
1. Define constants for naming convention:
   - ENVIRONMENT options: "dev", "staging", "prod"
   - SERVER_TYPE options: "web", "app", "db", "cache"
   - REGION options: "us-east", "us-west", "eu-central"

2. Ask user for:
   - Environment
   - Server type
   - Region
   - Instance number (1, 2, 3, etc.)

3. Generate hostname following pattern:
   {environment}-{server_type}-{region}-{number:02d}
   Example: prod-web-us-east-01

4. Convert all inputs to lowercase
5. Validate that number is between 1-99
6. Print the generated hostname

EXTRA: Generate 5 consecutive hostnames (01, 02, 03, 04, 05)
"""
