# istall required librabry
from twilio.rest import Client
from datetime import datetime,timedelta
import time
# twilio credentials
account_sid= 'AC2e2feba8d30866426b910ea705d11acc'
auth_token='df21141fca806f035701c562401c0d82'


client =Client(account_sid,auth_token)


# degine send messaGE function
def send_whatsapp_message(recipient_number,message_body):
    try:
        message =client.messages.create(
            from_='whatsapp:+14155238886' ,
            body = message_body ,
            to=f'whatsapp:{recipient_number}'
        )
        print('message sent successfully! Message SID{message.sid}')
    except Exception as e:
        print('An error occured')


# user input 
name= input("enter the recipient name: ")
recipient_number=input("enter the recipient whatsapp number with country code : ")
message_body=input("enter the message you want to send: ")
# date/time and calculate delay 
date_str= input("enter the date to send the message (YYYY-MM-DD): ")
time_str=input("enter the time to send message (HH:MM in  24hours format): ")



# datetime 
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime= datetime.now()

# calculate delay 
time_difference= schedule_datetime - current_datetime
delay_in_seconds=time_difference.total_seconds()


if delay_in_seconds <=0:
    print("scheduled time is in the past . please entre a future date and time: ")
else:
    print(f'message scheduled to be sent to {name} at {schedule_datetime}')



    # wait until the sceduled time 
    time.sleep(delay_in_seconds)

    # send the message 
    send_whatsapp_message( recipient_number,message_body)



