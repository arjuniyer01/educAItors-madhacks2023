import streamlit as st
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
import ssl
import time

ssl._create_default_https_context = ssl._create_unverified_context

SENDGRID_API_KEY = st.secrets["SENDGRID_API_KEY"]

# Using Twilio SendGrid's Python Library to send emails
def send_email(email, message, key):
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    from_email = Email("educaitors@gmail.com")
    to_email = To(email)
    subject = f"Team Educ-AI-tors: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(key)))}: {message[0:10]}..."
    content = Content("text/plain", message)
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    st.success(f"Email sent to {email}")
