import requests
from monitor_modules.config import NOTYFI_URL, NOTYFI_API_KEY, YOUR_NOTYFICO_NUMBER, SEND_TO

import os
from dotenv import load_dotenv


current_directory = os.getcwd()
# Load .env file from the current directory
dotenv_path = os.path.join(current_directory, ".env")
load_dotenv(dotenv_path)

def send_notification(message, tag=None):
    """Send an alert to Notyfi.co with the correct payload format."""
    
    headers = {
        "apikkey": os.getenv("NOTYFI_API_KEY")  # API key from the config
    }
    
    for to_phone_number in os.getenv("SEND_TO").split(","):
        # Create the payload with the mandatory fields first
        payload = {
            "from": os.getenv("YOUR_NOTYFICO_NUMBER"),  # Sender's phone number (example, you can change it)
            "to": to_phone_number,         # Recipient's phone number
            "message": message             # The message you want to send
        }

        # Add the 'tag' field only if it's provided
        if tag:
            payload["tag"] = tag

        # Send the request
        response = requests.post(NOTYFI_URL, json=payload, headers=headers)
        
        if response.status_code == 200:
            print(f"✅ Notification sent to {to_phone_number}: {message}")
        else:
            print(f"❌ Failed to send notification to {to_phone_number}: {response.text}")
