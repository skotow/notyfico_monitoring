import time
import psutil
import socket
import requests
from monitor_modules.notifier import send_notification

def check_service_exists(service_name):
    """Check if the service (process) exists on the system."""
    for proc in psutil.process_iter(['name']):
        if proc.info['name'].lower() == service_name.lower():
            return True
    return False

def check_service_running(service_name):
    """Check if the specific service is running."""
    for proc in psutil.process_iter(['name']):
        if proc.info['name'].lower() == service_name.lower():
            return True
    return False



def get_server_ip():
    """Get the local IP address of the server."""
    try:
       
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))  # Using Google DNS to get the external IP
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        return "Unable to get IP"

def get_server_hostname():
    """Get the hostname of the server."""
    return socket.gethostname()



def monitor_services(services, interval=900):
    print("Monitoring services")
    """Monitor a list of services."""
    while True:
        for service in services:
            if not check_service_exists(service):
                print(f"⚠️ Service {service} does not exist on the system.")
                continue  # Skip to the next service

            if not check_service_running(service):
                  # Get server IP and hostname
                server_ip = get_server_ip()
                server_hostname = get_server_hostname()
                server_info = f"Server: {server_hostname}\n\n({server_ip})"
                send_notification(f"⚠️ Service {server_info} is DOWN!")
            else:
                print(f"✅ Service {service} is running.")
        
        time.sleep(interval)
