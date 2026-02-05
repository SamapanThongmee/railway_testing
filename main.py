"""
Simple Telegram Test for Railway
"""
import requests
import datetime as dt
import os

# Use environment variables (set these in Railway Variables tab)
API_TOKEN = "8581449368:AAGizloFpLC7-DSKQsgqGs7kIiE3a44Czok" # os.getenv("TELEGRAM_API_TOKEN")
CHAT_ID = "7311904934" #os.getenv("TELEGRAM_CHAT_ID")

def send_message(message):
    """Send a message to Telegram"""
    if not API_TOKEN or not CHAT_ID:
        print("ERROR: TELEGRAM_API_TOKEN or TELEGRAM_CHAT_ID not set!")
        print("Please add these in Railway → Variables tab")
        return False
    
    api_url = f'https://api.telegram.org/bot{API_TOKEN}/sendMessage'
    try:
        response = requests.post(api_url, json={
            'chat_id': CHAT_ID, 
            'text': message,
            'parse_mode': 'HTML'
        })
        print(f"Response: {response.status_code}")
        if response.status_code == 200:
            print("Message sent successfully!")
        else:
            print(f"Failed: {response.text}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    """Main function"""
    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("="*50)
    print("Railway Telegram Test")
    print(f"Time: {now}")
    print("="*50)
    
    message = f"""Railway Cron Job Test

Time: {now}
Status: Running successfully!

This message confirms your Railway deployment is working."""
    
    success = send_message(message)
    
    print("="*50)
    print(f"Completed: {'SUCCESS' if success else 'FAILED'}")
    print("="*50)

if __name__ == "__main__":
    main()
