import psutil
import time
from datetime import datetime

LOG_FILE = "logs/system.log"
def log_message(message):
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")

def check_system():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = f"{timestamp} | CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%"

    print(status)
    log_message(status)

    if cpu > 80:
        alert = f"{timestamp} [ALERT] HIGH CPU USAGE"
        print(alert)
        log_message(alert)

    if memory > 75:
        alert = f"{timestamp} [ALERT] HIGH MEMORY USAGE"
        print(alert)
        log_message(alert)

    if disk > 90:
        alert = f"{timestamp} [ALERT] LOW DISK SPACE"
        print(alert)
        log_message(alert) 
while True:
    check_system()
    time.sleep(5)

