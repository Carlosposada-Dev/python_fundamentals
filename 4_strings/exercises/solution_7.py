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

# Your solution here
