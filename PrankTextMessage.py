from twilio.rest import Client

# Twilio account SID and auth token
account_sid = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# Twilio phone number
from_number = '+1234567890'

# Recipient's phone number
to_number = '+0987654321'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Send the text message
message = client.messages.create(
    to=to_number,
    from_=from_number,
    body='This is an automated text message.'
)

# Print the message SID
print(message.sid)