import psutil
import time
def get_load():
    all_cores_loads = psutil.cpu_percent(interval=None,percpu=True)
    return round(sum(all_cores_loads) / len(all_cores_loads),2)


# print(psutil.virtual_memory())

import psutil
import datetime

boot_time = psutil.boot_time()
print("Boot time (in seconds since epoch):", boot_time)

# Convert to human-readable format
boot_datetime = datetime.datetime.fromtimestamp(boot_time)
print("System boot time:", boot_datetime)
