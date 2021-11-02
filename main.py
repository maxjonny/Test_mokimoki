
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import requests
import config

def email(mail_text):
# create message object instance
    msg = MIMEMultipart()


    message = mail_text

    # setup the parameters of the message
    password = config.mail_password
    msg['From'] = config.mail_from
    msg['To'] = config.mail_to
    msg['Subject'] = "Тест на функцию"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)


    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print("successfully sent email to %s:" % (msg['To']))

def send_telegram(text: str):
    token = config.token
    url = "https://api.telegram.org/bot"
    channel_id = config.channel_id
    url += token
    method = url + "/sendMessage"
    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": text
        })
    print(r.status_code)
    if r.status_code != 200:
        raise Exception("post_text error")







