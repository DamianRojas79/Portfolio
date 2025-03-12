from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from decouple import config

app=Flask(__name__)

app.config['MAIL_SERVER']= config('MAIL_SERVER')
app.config['MAIL_PORT'] = config('MAIL_PORT')
app.config['MAIL_USERNAME'] = config('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = config('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail=Mail(app)


@app.route ('/')
def index():
    return render_template ('index.html')

@app.route('/mail', methods=['GET','POST'])
def send_mail():
    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        message=request.form.get('message')

        msg=Message(
            'Hola Damian, tienes un nuevo contacto desde la web:',
            body=f'Nombre: {name} \nCorreo: <{email}> \n\nEscribió: \n\n{message}',
            sender=email,
            recipients=['damianrojas@mailtrap.io']
        )
        mail.send(msg)
        return render_template('send_mail.html')


    return redirect(url_for('index'))
        

if __name__ == '__main__':
    app.run(debug=True)