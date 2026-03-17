import psutil
import time

def check_usage(name, value):

    if value > 90:
        print(name, "CRITICAL")
    elif value > 80:
        print(name, "WARNING")
    else:
        print(name, "OK")

cpu = psutil.cpu_percent()
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

print("System Status")
print("-------------")

print(f"CPU Usage: {cpu}%")
print(f"Memory Usage: {memory}%")
print(f"Disk Usage: {disk}%")

if cpu > 90 or memory > 90 or disk > 90:
    print("ALERT: SERVER PROBLEM")
    
elif cpu > 80 or memory > 80 or disk > 80:
    print("WARNING")

