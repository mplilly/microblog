import os
from flask import Flask
from flask_mail import (Mail, Message)

app = Flask(__name__)
mail = Mail(app)

app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    mail_use_ssl=True,
    mail_username=os.getenv('MAIL_ADDRESS'),
    mail_password=os.getenv('MAIL_PASSWORD')
)

mail=Mail(app)

@app.route('/')
def index():
    msg = Message(
        'subject body',
        sender='mpldev314@gmail.com',
        recipients=['mpldev314@gmail.com'])
    msg.body = 'message body'
    mail.send(msg)
    return 'Sent'

if __name__=='__main__':
    app.run()
