from src.fetch_data.networkd_data import get_mac_address
from src.fetch_data.memory_data import get_mem_data
from src.fetch_data.cpu_data import get_cpu_info, get_os_type, get_cpu_load

def get_data():
    mac = get_mac_address()
    mem_data = get_mem_data()
    cpu_data = get_cpu_info()
    data = {
        "mac": mac,
        "freeMemory": mem_data['free_mem'],
        "totalMemory": mem_data['total_mem'],
        "inUseMem": mem_data['in_use_mem'],
        "memUsage": mem_data['mem_per'],
        "osType": get_os_type(),
        "upTime": cpu_data['up_time'],
        "cpuType": cpu_data['cpu_type'],
        "numCores": cpu_data['num_cores'],
        "cpuSpeed": cpu_data['cpu_speed'],
        "cpuLoad": get_cpu_load()  # Replace with a live value
    }
    return data