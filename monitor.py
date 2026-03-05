import psutil

print("Server Health Monitoring")
print("------------------------")
print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
print(f"Memory Usage: {psutil.virtual_memory().percent}%")
print(f"Disk Usage: {psutil.disk_usage('/').percent}%")

