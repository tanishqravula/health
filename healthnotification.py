# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC43ec2a5124b04a86b9f13c4c55f6aa03"
auth_token = "b84b8a8fd0a3969d1d9fc4e13df28b27"
client = Client(account_sid, auth_token)

message = client.messages.create(
  body="Hello from Family Medical. This is just a reminder alert. Have a nice day.",
  from_="+12765229583",
  to="+917702337176"
)

print(message.sid)