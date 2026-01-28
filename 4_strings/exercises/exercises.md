# Section 4: Strings - Practical Exercises

## General Instructions
- Follow PEP 8 conventions (naming, spacing)
- Use descriptive variable names in snake_case
- Define constants in UPPER_SNAKE_CASE
- Prefer f-strings for formatting
- Use appropriate string methods for each task

---

## Exercise 1: Log Parser - Extract Information
**Difficulty:** Easy  
**Objective:** Practice string slicing and basic methods

Parse a log entry to extract key information:
- Date (first 10 characters)
- Time (characters 11-19)
- Log level, Server name, Error message

**Example:**
```
log = "2024-01-15 14:30:45 ERROR web-server-01 Connection timeout after 30s"
Output:
  Date: 2024-01-15
  Time: 14:30:45
  Level: ERROR
  Server: web-server-01
  Message: Connection timeout after 30s
```

---

## Exercise 2: AWS ARN Parser
**Difficulty:** Easy-Medium  
**Objective:** Practice split() and indexing

Parse an AWS ARN to extract components:
- Partition, Service, Region, Account ID, Resource

**Example:**
```
arn = "arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0"
ARN format: arn:partition:service:region:account-id:resource
```

---

## Exercise 3: Server Hostname Generator
**Difficulty:** Medium  
**Objective:** Practice string formatting and concatenation

Generate standardized server hostnames following pattern:
`{environment}-{server_type}-{region}-{number:02d}`

**Example:** `prod-web-us-east-01`

Inputs: environment, server type, region, instance number (1-99)

---

## Exercise 4: Config File Key-Value Parser
**Difficulty:** Medium  
**Objective:** Practice split(), strip(), and string manipulation

Parse configuration strings in INI-like format:
```
config = "server=192.168.1.100 ; port=8080 ; ssl=true ; timeout=30"
```

Extract and convert: Server IP, Port (integer), SSL (boolean), Timeout

---

## Exercise 5: IP Address Validator (Basic)
**Difficulty:** Medium  
**Objective:** Practice split(), isdigit(), and validation logic

Validate IPv4 addresses:
- Must have exactly 4 octets separated by dots
- Each octet must be a number between 0-255

**Test cases:**
- "192.168.1.1" → Valid
- "192.168.1.256" → Invalid (256 > 255)
- "192.168.1" → Invalid (only 3 octets)
- "192.168.1.abc" → Invalid (not a number)

---

## Exercise 6: Log Level Counter and Filter
**Difficulty:** Medium-Hard  
**Objective:** Practice string searching, counting, and filtering

Analyze multiple log entries and:
- Count occurrences of each log level (INFO, WARNING, ERROR)
- Filter and display only ERROR logs
- Create a summary report with counts and ERROR details

---

## Exercise 7: Docker Command Builder
**Difficulty:** Medium-Hard  
**Objective:** Practice string formatting, join(), and building complex strings

Generate Docker run commands with:
- Container name, Image name, Host/Container ports
- Environment variables, Volume mounts

**Output example:**
```
docker run -d \
  --name web-server \
  -p 8080:80 \
  -e ENV=prod \
  -e DEBUG=false \
  -v /data:/app/data \
  -v /logs:/app/logs \
  nginx:latest
```

---

## Instructions
1. Solve each exercise in its corresponding solution_X.py file
2. Apply PEP 8 and Clean Code principles
3. Test with different inputs
4. Consider edge cases
