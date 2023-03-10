from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxx"
# Your Auth Token from twilio.com/console
auth_token  = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_="xxxxxxxxxxxxxxxxxxxxx", 
    to="xxxxxxxxxxxxxxxxxxxxxxxx",
    body="Hello from Python!")

print(message.sid)