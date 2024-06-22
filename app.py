from flask import Flask, render_template
from flask_mail import Mail, Message

app=Flask(__name__)

app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'aad8bfe78c51f3'
app.config['MAIL_PASSWORD'] = '565a1f1c6911a5'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail=Mail(app)


@app.route ('/')
def index():
    return render_template ('index.html')

@app.route('/mail')
def send_mail():
    return render_template('send_mail.html')