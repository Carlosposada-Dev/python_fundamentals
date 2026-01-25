"""
## Exercise 1: AWS EC2 Cost Calculator

**Difficulty**: Beginner  
**Objective**: Practice basic arithmetic operators  
**Context**: Calculate monthly cost of EC2 instances

### TODO:

1. Define constants:
   - Hours per month: 730
   - Cost per hour for t3.medium instance: $0.0416

2. Request from the user the number of instances to deploy
3. Calculate:
   - Monthly cost per instance
   - Total monthly cost (all instances)
   - Annual cost (12 months)

4. Print results with 2 decimal places
   - Suggested format: `"Cost per instance per month: $30.37"`

"""

HOURS_PER_MONTH = 730
COST_PER_HOUR_T3_MEDIUM = 0.0416

number_of_instances = int(input("Please, enter the number of instances to deploy: "))
cost_per_month_of_t3_instance = HOURS_PER_MONTH * COST_PER_HOUR_T3_MEDIUM
total_monthly_cost = cost_per_month_of_t3_instance * number_of_instances
annual_cost = total_monthly_cost * 12

print(f"AWS COST CALCULATOR\n")
print(f"Monthly cost per t3 instance: ${cost_per_month_of_t3_instance:.2f}")
print(f"Total monthly cost for {number_of_instances} t3 instance(s):${total_monthly_cost:.2f}")
print(f"Annual cost for {number_of_instances} t3 instance(s): ${annual_cost:.2f}")
