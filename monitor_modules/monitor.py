import psutil
import time
import socket
import requests
from monitor_modules.notifier import send_notification
# from monitor_modules.config import THRESHOLD_CPU, THRESHOLD_MEM, THRESHOLD_DISK, ENABLE_AVARAGE_LOAD
import os
from dotenv import load_dotenv


current_directory = os.getcwd()
# Load .env file from the current directory
dotenv_path = os.path.join(current_directory, ".env")
load_dotenv(dotenv_path)



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

def monitor_system(interval=900):
    print("Monitoring started...")
    while True:
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        # Get load averages (1, 5, 15 minutes)
        load_1min, load_5min, load_15min = psutil.getloadavg()

        # Get the number of CPU cores
        num_cores = psutil.cpu_count()
        
        # Define load average thresholds based on the number of cores
        load_threshold = 1.5 * num_cores  # Load average should not exceed 1.5 * number of cores for a warning

        # Get server IP and hostname
        server_ip = get_server_ip()
        server_hostname = get_server_hostname()

        # Add IP and hostname information to the message
        server_info = f"Server: {server_hostname}\n\n({server_ip})"

        # Check for resource usage thresholds and send notifications
        if cpu_usage > int(os.getenv('THRESHOLD_CPU')):
            send_notification(f"{server_info}\n\n🚨 High CPU Usage: {cpu_usage}%", 'server_high_cpu')

        if memory_usage > int(os.getenv('THRESHOLD_MEM')):
            send_notification(f"{server_info}\n\n🚨 High Memory Usage: {memory_usage}%",'memory_usage_warning')

        if disk_usage > int(os.getenv('THRESHOLD_DISK')):
            send_notification(f"{server_info}\n\n🚨 High Disk Usage: {disk_usage}%",'disk_usage_warning')
        
        # If load average exceeds threshold, send a notification
        if os.getenv('ENABLE_AVARAGE_LOAD'):
            if load_1min > load_threshold:
                send_notification(f"{server_info}\n\n🚨 High Load Average (1 min): {load_1min}",'avg_load_warnings')
            if load_5min > load_threshold:
                send_notification(f"{server_info}\n\n🚨 High Load Average (5 min): {load_5min}",'avg_load_warnings')
            if load_15min > load_threshold:
                send_notification(f"{server_info}\n\n🚨 High Load Average (15 min): {load_15min}",'avg_load_warnings')
        
        time.sleep(interval)
