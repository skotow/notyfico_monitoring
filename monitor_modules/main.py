import threading
from monitor_modules.monitor import monitor_system
from monitor_modules.service_checker import monitor_services
import os
from dotenv import load_dotenv


current_directory = os.getcwd()
# Load .env file from the current directory
dotenv_path = os.path.join(current_directory, ".env")

print("sssssssssss",dotenv_path)
load_dotenv(dotenv_path)

def start_monitoring_system():
    monitor_system(interval=int(os.getenv('INTERVAL_MONITOR', 900)))  # Monitor system resources like CPU, Memory, Disk

def start_monitoring_services():
    services_to_monitor = os.getenv("SERVICES_TO_MONITOR").split(',')
    monitor_services(services_to_monitor, interval=int(os.getenv('INTERVAL_SERVICE', 900)))  # Monitor services

def main():
    # Start monitoring system in a separate thread
    system_thread = threading.Thread(target=start_monitoring_system)
    system_thread.start()

    # Start monitoring services in a separate thread
    services_thread = threading.Thread(target=start_monitoring_services)
    services_thread.start()

if __name__ == "__main__":
    main()