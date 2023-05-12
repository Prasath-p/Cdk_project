import os
from email.message import EmailMessage 
import ssl
import smtplib
email_sender = "prasath201907@gmail.com"
email_pass = "zbnspzgnkigryqjv"
email_recv = "sanjay2019cs@gmail.com"

subject = "check out"
body = """ <h1> email working </h1>  """

em = EmailMessage()

em['From'] = email_sender
em['To'] = email_recv
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_pass)
    smtp.sendmail(email_sender, email_recv, em.as_string())

