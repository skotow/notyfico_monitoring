import threading
from monitor_modules.monitor import monitor_system
from monitor_modules.service_checker import monitor_services
from monitor_modules.notifier import send_notification
import os
import argparse
from dotenv import load_dotenv


current_directory = os.getcwd()
# Load .env file from the current directory
dotenv_path = os.path.join(current_directory, ".env")

load_dotenv(dotenv_path)

def main():
    print("Sending notification")
    parser = argparse.ArgumentParser(description="Send an inline message via Notyfi.co")
    parser.add_argument("message", type=str, help="The message to send")
    parser.add_argument("tag", type=str, help="Tag your message")

    args = parser.parse_args()

    send_notification(args.message,args.tag)


if __name__ == "__main__":
    main()