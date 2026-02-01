"""
Exercise 4: Config File Key-Value Parser
Difficulty: Medium
Objective: Practice split(), strip(), and string manipulation

Context: Parse configuration strings in INI-like format.

Task:
1. Given a configuration string:
   config = "server=192.168.1.100 ; port=8080 ; ssl=true ; timeout=30"

2. Parse the config by:
   - Split by ';' to get individual settings
   - For each setting, split by '=' to get key and value
   - Strip whitespace from keys and values

3. Store in variables or print each setting:
   Server: 192.168.1.100
   Port: 8080
   SSL: true
   Timeout: 30

4. Convert the port to integer
5. Convert ssl string to boolean (True if "true", False if "false")

EXTRA: Handle case where user provides config with different spacing
"""

# The solution it's developing only with the concepts that have been seen until this point.



print("\nCONFIG FILE KEY-VALUE PARSER\n")

config = input("Enter configuration string: (e.g:server=192.168.1.100 ; port=8080 ; ssl=true ; timeout=30): ")
if config.count("=") != 4 or config.count(";") != 3:
   print("Error: Only server, port, ssl and timeout are allowed")
   exit()

# validation fase

WHITELIST = ["server", "port", "ssl", "timeout"]
part_1, part_2, part_3, part_4 = config.split(" ; ")

part_1 = part_1.strip()
part_2 = part_2.strip()
part_3 = part_3.strip()
part_4 = part_4.strip()

key_1, value_1 = part_1.split("=")
key_2, value_2 = part_2.split("=")
key_3, value_3 = part_3.split("=")
key_4, value_4 = part_4.split("=")

key_1 = key_1.strip()
value_1 = value_1.strip()
key_2 = key_2.strip()
value_2 = value_2.strip()
key_3 = key_3.strip()
value_3 = value_3.strip()
key_4 = key_4.strip()
value_4 = value_4.strip()

if (key_1 != "server") or (key_2 != "port") or (key_3 != "ssl") or (key_4 != "timeout"):
   print("Error: Keys must be in order: server, port, ssl, timeout")
   exit()

if (key_1 not in WHITELIST) or (key_2 not in WHITELIST) or (key_3 not in WHITELIST) or (key_4 not in WHITELIST):
   print("Error: Only server, port, ssl and timeout are allowed")
   exit()
   
if (key_1 == "server"):
    if value_1.replace(".","").isdigit() == False:
        print("Error: server value must be an IP address")
        exit()
elif (key_2 =="port"):
    if value_2.isdigit() == False:
        print("Error: port value must be an integer")
        exit()
elif (key_3 == "ssl"):
    if (value_3 != "true") and (value_3 != "false"):
        print("Error: ssl value must be true or false")
        exit()
else:
    if value_4.isdigit() == False:
        print("Error: timeout value must be an integer")
        exit()

print("\nParsed Configuration:\n")
print(f"Server: {value_1}")
print(f"Port: {int(value_2)}")
print(f"SSL: {True if value_3 == 'true' else False}")
print(f"Timeout: {int(value_4)}")