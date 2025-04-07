import psutil
import socket

def get_mac_address():
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