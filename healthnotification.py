import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC43ec2a5124b04a86b9f13c4c55f6aa03"
auth_token = "1e6fe68db284b1217f5e735bcd701f5d"
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="Hello from Family Medical.Feel free to ask if you have any queries.or else let us have a meet through this https://tanishqravula.github.io/tanishq/REMO/video.html and send meeting link to us through tanishqravula@gmail.com",
  from_="+12765229583",
  to="+917702337176"
)
print(message.sid)
