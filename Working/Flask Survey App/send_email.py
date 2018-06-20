from email.mime.text import MIMEText
import smtplib

def send_email(email, name,number):
    from_email=input("password::email")
    from_password=input("password::")
    to_email=email

    subject="Re: invitation"
    message= "{},,{}".format(name,number)
    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
