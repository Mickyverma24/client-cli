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


# async def get_cpu_load():
#     start = cpu_average()
#     await asyncio.sleep(0.1)  # 100ms delay
#     end = cpu_average()
#     idle_diff = end["idle"] - start["idle"]
#     total_diff = end["total"] - start["total"]
#     percentage_of_cpu = 100 - int((100 * idle_diff) / total_diff)
#     return percentage_of_cpu

if __name__ == "__main__":
    print(get_cpu_info())

