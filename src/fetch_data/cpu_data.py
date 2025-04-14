import platform
import psutil

def get_os_type():
    return platform.system()

def get_cpu_info():
    up_time = psutil.boot_time()
    cpu_info = psutil.cpu_freq()
    num_cores = psutil.cpu_count(logical=False) or 1
    cpu_speed = cpu_info.max if cpu_info else None
    cpu_type = platform.processor()
    return {
        "up_time" : up_time,
        "num_cores" : num_cores,
        "cpu_speed" : cpu_speed,
        "cpu_type" : cpu_type,
    }

def get_cpu_load():
    return psutil.cpu_percent(interval=1)
if __name__ == "__main__":
    print(get_cpu_info())

