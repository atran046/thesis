import sys
from twilio.rest import TwilioRestClient
from multiprocessing import Event
import database




# Twilio Account Details

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
#------------------------------------------------------------------------
# Sending the Text Messages
def send_cmd(Event):
    for x in range(1,10):
        message = client.messages.create(
            body = database.retrieve(x),
            )
    print (message.sid)
    #cursor = database.main()
    


# Receiving the text messages -----------------------------------------



def quit_app(Event):
    root.quit()

