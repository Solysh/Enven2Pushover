import http.client
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
PUSHOVER_USER_KEY = os.getenv('PUSHOVER_USER_KEY')
PUSHOVER_API_TOKEN = os.getenv('PUSHOVER_API_TOKEN')

def send_pushover_notification(message, image_url=None):
    print(f'Pushover called')
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    body = {
        "token": PUSHOVER_API_TOKEN,
        "user": PUSHOVER_USER_KEY,
        "message": message,
        "html": 1  # Enable HTML formatting
    }
    
    if image_url:
        body["attachment"] = image_url

    conn.request("POST", "/1/messages.json",
                 body=json.dumps(body),
                 headers={"Content-Type": "application/json"})
    
    response = conn.getresponse()
    print(f'Pushover sent')
    return response.status, response.reason