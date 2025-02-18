from flask import current_app, render_template
from flask_mail import Mail, Message

mail = Mail()

def init_mail(app):
    mail.init_app(app)

def send_email(subject, recipient, template, **kwargs):
    msg = Message(subject, recipients=[recipient], sender=current_app.config['MAIL_DEFAULT_SENDER'])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)