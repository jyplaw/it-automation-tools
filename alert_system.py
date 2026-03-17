def send_alert(message):
    print("ALERT:", message)

import psutil

cpu = psutil.cpu_percent()

if cpu > 90:
    send_alert("CPU CRITICAL")
elif cpu > 80:
    send_alert("CPU WARNING")