from twilio.rest import Client

account_sid = "AC83e3c0d39086dfbc88a3be57c9d53639"
auth_token = "your_auth_token"

client = Client(account_sid, auth_token)

fax = client.fax.v1.faxes.create(
    from_="+15017250604",
    to="+15558675309",
    media_url="https://www.twilio.com/docs/documents/25/justthefaxmaam.pdf")

print(fax.sid)
