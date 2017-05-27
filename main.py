import sys
from twilio.rest import TwilioRestClient
from multiprocessing import Event
import database




# Twilio Account Details
ACCOUNT_SID = "AC5149d33e538a72c194a70f1b702db479"
AUTH_TOKEN = "0385315cb14c37f2cc34350a24e1b979"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
#------------------------------------------------------------------------
# Sending the Text Messages
def send_cmd(Event):
    for x in range(1,10):
        message = client.messages.create(
            body = database.retrieve(x),
            to="+18053729380",
            from_="+18054448126",
            )
    print (message.sid)
    #cursor = database.main()
    


# Receiving the text messages -----------------------------------------



def quit_app(Event):
    root.quit()

