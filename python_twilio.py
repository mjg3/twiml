from twilio.rest import Client


# Your Account SID from twilio.com/console
account_sid = "AC17aff2a74960a87c99ce7037342c1982"
# Your Auth Token from twilio.com/console
auth_token  = "2900ed6c5c3dff153f90fee834d37a82"

client = Client(account_sid, auth_token)

call = client.calls.create(
    to="+19737382206",
    from_="+18026130730",
    url="/"
)

print(call.sid)
