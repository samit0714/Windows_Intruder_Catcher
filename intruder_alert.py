import cv2
import requests
import time
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv 

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

EMAIL_ID = os.getenv("EMAIL_ID")
APP_PASSWORD = os.getenv("APP_PASSWORD")

def send_email_alert(photo_path):
    print("Hostel Wi-Fi blocked Telegram. Bypassing via Email...")
    msg = EmailMessage()
    msg['Subject'] = '🚨 URGENT: Someone Trying To Unlock Your Laptop....!'
    msg['From'] = EMAIL_ID
    msg['To'] = EMAIL_ID  
    msg.set_content("Alert! Someone tried to access your laptop. See attached photo.")

    with open(photo_path, 'rb') as f:
        img_data = f.read()
    msg.add_attachment(img_data, maintype='image', subtype='jpeg', filename='intruder.jpg')

    try:
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ID, APP_PASSWORD)
            smtp.send_message(msg)
        print("Bypass Successful: Email delivered!")
    except Exception as e:
        print(f"Email failed: {e}")

def catch_intruder():
    print("Camera warming up...")
    cap = cv2.VideoCapture(0)
    time.sleep(2)
    ret, frame = cap.read()
    cap.release()

    if ret:
        photo_path = "alert.jpg"
        cv2.imwrite(photo_path, frame)
        
        
        url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
        try:
            with open(photo_path, 'rb') as photo:
                payload = {'chat_id': CHAT_ID, 'caption': '🚨 ALERT: Intruder Detected!'}
                files = {'photo': photo}
                response = requests.post(url, data=payload, files=files, timeout=5)
            
            if response.status_code == 200:
                print("Mission Successful: Telegram par alert gaya!")
            else:
                
                send_email_alert(photo_path)
        except requests.exceptions.RequestException:
            
            send_email_alert(photo_path)
            
        if os.path.exists(photo_path):
            os.remove(photo_path)

if __name__ == "__main__":
    catch_intruder()