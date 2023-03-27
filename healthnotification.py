import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC43ec2a5124b04a86b9f13c4c55f6aa03"
auth_token = "1c24139daf9aeb4f5760251ea8ad9b12"
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="Hello from Twilio",
  from_="+12765229583",
  to="+917702337176"
)
print(message.sid)
