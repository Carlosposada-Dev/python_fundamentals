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
# The solution it's developing only with the concepts that have been seen until this point.

DEV_ENVIRONMENT = "dev"
STG_ENVIRONMENT ="staging"
PRD_ENVIRONMENT = "prod"

SERVER_TYPE_WEB = "web"
SERVER_TYPE_APP = "app"
SERVER_TYPE_DB = "db"
SERVER_TYPE_CACHE = "cache"

REGION_US_EAST = "us-east"
REGION_US_WEST = "us-west"
REGION_EU_CENTRAL = "eu-central"


# Your solution here
print("\nSERVER HOSTNAME GENERATOR\n")

environment = input("Enter environment (dev, staging, prod): ").lower()
if environment not in [DEV_ENVIRONMENT, STG_ENVIRONMENT, PRD_ENVIRONMENT]:
   print("Invalid environment. Please enter dev, staging or prod.")
   exit()
server_type = input("Enter server type (web, app, db, cache): ").lower()
if server_type not in [SERVER_TYPE_WEB, SERVER_TYPE_APP, SERVER_TYPE_DB, SERVER_TYPE_CACHE]:
   print("Invalid server type. Please enter web, app, db, or cache.")
   exit()
region = input("Enter region( us-east, us-west, eu-central): ").lower()
if region not in [REGION_US_EAST, REGION_US_WEST, REGION_EU_CENTRAL]:
   print("Invalid region. Please enter us-east, us-west or eu-central.")
   exit()
instance_number = int(input("Enter number of instances (must be between 1 and 99): "))
if instance_number < 1 or instance_number > 99:
   print("Invalid number of instances. Must be between 1 and 99.")
   exit()

generate_hostname_1 = f"{environment}-{server_type}-{region}-{instance_number:02d}"
generate_hostname_2 = f"{environment}-{server_type}-{region}-{instance_number+1:02d}"
generate_hostname_3 = f"{environment}-{server_type}-{region}-{instance_number+2:02d}"
generate_hostname_4 = f"{environment}-{server_type}-{region}-{instance_number+3:02d}"
generate_hostname_5 = f"{environment}-{server_type}-{region}-{instance_number+4:02d}"
print("\nGenerated Hostnames:\n")
print(f"1. {generate_hostname_1}")
print(f"2. {generate_hostname_2}")
print(f"3. {generate_hostname_3}")
print(f"4. {generate_hostname_4}")
print(f"5. {generate_hostname_5}")
