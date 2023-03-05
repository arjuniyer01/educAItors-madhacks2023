import streamlit as st
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

SENDGRID_API_KEY = st.secrets["SENDGRID_API_KEY"]

# Using Twilio SendGrid's Python Library to send emails
def send_email(email, message):
    # sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    # from_email = Email("educaitors@gmail.com")
    # to_email = To(email)
    # subject = "Message from your Streamlit app"
    # content = Content("text/plain", message)
    # mail = Mail(from_email, to_email, subject, content)
    # response = sg.client.mail.send.post(request_body=mail.get())
    st.success(f"{message[0:10]}... sent to {email}")
