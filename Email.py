from flask import Flask
from flask_mail import Mail, Message

def send_email(to, subject, template):
    mail = Mail()
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender='ErythrocyteBloodDonations@gmail.com'
    )
    mail.send(msg)
