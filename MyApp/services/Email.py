import smtplib
from email.message import EmailMessage
import ssl

from utilities.constants import SUBJECT, BODY

def send_email(data):
    ''' Function to send email '''
    email_sender=' Sender Email Address'
    email_password= " Secreat Password"
    email_receiver = 'Reciver Email Address'
    
    email = EmailMessage()

    email['From'] = email_sender
    email['To'] = email_receiver
    email['Subject']= SUBJECT

    content = BODY + f'{data}'
    email.set_content(content)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail (email_sender, email_receiver, email.as_string())

    return email_receiver