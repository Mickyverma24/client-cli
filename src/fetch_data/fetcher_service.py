import platform
import psutil
import socket

# optimiaztion to-do ( some data is static fetch that data only once and use it again and again rest data get each time)

class MonitoringData:
    def __init__(self):
        pass

    def get_os_type(self):
        return platform.system()

    def get_cpu_info(self):
        up_time = psutil.boot_time() # this is creating some false information needs to be imporved
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

    def get_cpu_load(self):
        """this will provide the load of the cpu in 1 second interval"""
        return psutil.cpu_percent(interval=0.7)

    def get_host_name(self):
        """Getting the name of the owner of the server."""
        host = socket.gethostname()
        return host if host else "Someone unknown"
    
    def get_mem_data(self):    
        data = psutil.virtual_memory()
        return {
            'free_mem': data.available,
            'total_mem': data.total,
            'in_use_mem': data.used,
            'mem_per': data.percent / 100
        }

    def get_mac_address(self):
    # Find the active network interface (used for internet access)
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))  # Google's DNS (used just to get the route)
            active_interface_ip_address = s.getsockname()[0] # Get the IP of the active interface and the port

        interface_properties = psutil.net_if_addrs()

        # Find which interface has this IP
        interface_name = None
        for interface, addrs in interface_properties.items():
            for addr in addrs:
                if addr.family == socket.AF_INET and addr.address == active_interface_ip_address:
                    interface_name = interface
                    break
            if interface_name:
                break  # Exit once we find the correct interface

        # # Get the MAC address of the active interface
        if interface_name:
            for addr in interface_properties[interface_name]:
                if addr.family == psutil.AF_LINK:
                    return addr.address
        return None