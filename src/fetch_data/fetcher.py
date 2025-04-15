from src.fetch_data.fetcher_service import MonitoringData


fetcher = MonitoringData()

def get_data():
    mac = fetcher.get_mac_address()
    mem_data = fetcher.get_mem_data()
    cpu_data = fetcher.get_cpu_info()
    data = {
        "mac": mac,
        "freeMemory": mem_data['free_mem'],
        "totalMemory": mem_data['total_mem'],
        "inUseMem": mem_data['in_use_mem'],
        "memUsage": mem_data['mem_per'],
        "osType": fetcher.get_os_type(),
        "upTime": cpu_data['up_time'],
        "cpuType": cpu_data['cpu_type'],
        "numCores": cpu_data['num_cores'],
        "cpuSpeed": cpu_data['cpu_speed'],
        "cpuLoad": fetcher.get_cpu_load()  
    }
    return data
