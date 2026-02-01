"""
Exercise 7: Docker Command Builder
Difficulty: Medium-Hard
Objective: Practice string formatting, join(), and building complex strings

Context: Generate Docker run commands with multiple options.

Task:
1. Ask user for:
   - Container name
   - Image name (e.g., "nginx:latest")
   - Host port
   - Container port
   - Environment variables (comma-separated, e.g., "ENV=prod,DEBUG=false")
   - Volume mounts (comma-separated, e.g., "/data:/app/data,/logs:/app/logs")

2. Build a docker run command with this structure:
   docker run -d --name {name} -p {host_port}:{container_port} \\
     -e {env1} -e {env2} \\
     -v {volume1} -v {volume2} \\
     {image}

3. Process the inputs:
   - Split environment variables and volume mounts by comma
   - Format each env var with -e flag
   - Format each volume with -v flag
   - Use join() to combine them

4. Print the final command (can be multi-line for readability)

Example output:
   docker run -d \\
     --name web-server \\
     -p 8080:80 \\
     -e ENV=prod \\
     -e DEBUG=false \\
     -v /data:/app/data \\
     -v /logs:/app/logs \\
     nginx:latest

EXTRA: Add --restart=always and --network options
"""

# The solution it's developing only with the concepts that have been seen until this point.

print("\nDOCKER COMMAND BUILDER\n")

container_name = input("Enter container name: ")
image_name = input("Enter image name (e.g., 'nginx:latest or nginx:alpine'): ")
host_port = int(input("Enter host port: "))
container_port = int(input("Enter container port: "))
env_vars_input = input("Enter environment variables (Max two, comma-separated, e.g., 'ENV=prod,DEBUG=false'): ")
if "," not in env_vars_input:
   print("Please enter two environment variables separated by a comma.")
   exit() 
env_var_1, env_var_2 = env_vars_input.split(",")
volume_mounts_input = input("Enter volume mounts (Max, comma-separated, e.g., '/data:/app/data,/logs:/app/logs'): ")
if "," not in volume_mounts_input:
   print("Please enter two volume mounts separated by a comma.")
   exit()
volume_mount_1, volume_mount_2 = volume_mounts_input.split(",")

first_line = f"docker run -d \\\n  --name {container_name} \\\n  -p {host_port}:{container_port} \\"
env_lines = f"  -e {env_var_1.strip()} \\\n  -e {env_var_2.strip()} \\"
volume_lines = f"  -v {volume_mount_1.strip()} \\\n  -v {volume_mount_2.strip()} \\"
image_name_line = f"  {image_name}"

docker_command = f"{first_line}\n{env_lines}\n{volume_lines}\n{image_name_line}"

print("\nGenerated Docker Command:\n")
print(docker_command)
