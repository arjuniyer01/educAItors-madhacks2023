from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid = "ACe6863cf6c8939e9e5f15005503d5f1f9"
auth_token = "3036d6a2fd9e044569062c54a61f0ceb"

# The WhatsApp number you want to send the message to
to_whatsapp_number = "whatsapp:+16086224320"

# Initialize the Twilio client
client = Client(account_sid, auth_token)

# Send a WhatsApp message
message = client.messages.create(
    from_="whatsapp:+14155238886", body="Hello from Twilio!", to=to_whatsapp_number
)

# Send a voice clip as a message
# message = client.messages.create(
# from_='whatsapp:+14155238886',
# media_url="https://example.com/voiceclip.mp3",
# to=to_whatsapp_number
# )
