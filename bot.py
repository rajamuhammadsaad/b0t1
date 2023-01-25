from twilio.rest import Client
import schedule
import time

# Twilio account information
account_sid = 'AC22a5990ba4fe70610d76b08e40f90c5f'
auth_token = 'bc92a9ca8352909870a0f8ea149897de'
client = Client(account_sid, auth_token)

# Your WhatsApp number
whatsapp_number = 'whatsapp:+14155238886'

# Function to send a reminder message
def send_reminder():
    message = client.messages.create(
        body='Don\'t forget to take your medicine!',
        from_=whatsapp_number,
        to='whatsapp:+3209342040'
    )
    print(message.sid)

# Schedule the reminder to be sent at a specific time every day
schedule.every().day.at("10:30").do(send_reminder)

while True:
    schedule.run_pending()
    time.sleep(1)
