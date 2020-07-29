#!/usr/bin/env python3
# text_myself.py - Defines the textmyself() function that texts a message
# passed to it as a string.

# Please fill out preset values with your account info.
# Preset values:
accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
my_number = '+15559998888'
twilio_num = '+15552225678'

from twilio.rest import Client
def text_myself(message):
    twilioCli = Client(accountSID, auth_token)
    twilioCli.messages.create(body=message, from_=twilio_num, to=my_number)
