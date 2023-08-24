import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC57b15b2f874c753f76cd667a0712be0b"
auth_token = "14626d8bce8144cce9a4f7be04d62400"
client = Client(account_sid, auth_token)
message = client.messages.create(
   body="Hello from Family Medical.Feel free to ask if you have any queries.or else let us have a meet through this https://tanishqravula.github.io/tanishq/REMO/video.html and send meeting link to us through tanishqravula@gmail.com",
  from_="+19897109806",
  to="+917702337176"
)
print(message.sid)
