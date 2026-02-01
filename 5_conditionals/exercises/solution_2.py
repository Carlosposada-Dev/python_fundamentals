"""
Exercise 2: AWS ARN Parser
Difficulty: Easy-Medium
Objective: Practice split() and indexing

Context: Parse an AWS ARN to extract components.

Task:
1. Given an ARN (Amazon Resource Name):
   arn = "arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0"

2. ARN format is: arn:partition:service:region:account-id:resource
   Use split(':') to break it apart

3. Extract and print:
   - Partition (aws, aws-cn, aws-us-gov)
   - Service (ec2, s3, lambda, etc.)
   - Region (us-east-1, eu-west-1, etc.)
   - Account ID
   - Resource type and ID

4. Handle the resource part (may contain / or :)

EXTRA: Ask the user for an ARN and parse it
"""

# Your solution here

print("\nAWS ARN PARSER\n")
arn = input("Enter an AWS ARN: ")

parts = arn.split(":")

if len(parts) < 6 or parts[0] != "arn":
    print("Invalid ARN format. Please verify and try again.")
else:
    partition = parts[1]
    service = parts[2]
    region = parts[3]
    account_id =parts[4]
    resource = parts[5]
    print(f"\nElements of the ARN:\n")
    print(f"Partition: {partition}")
    print(f"Service: {service}")
    print(f"Region: {region}")
    print(f"Account ID: {account_id}")
    print(f"Resource: {resource}")