from flask import render_template
from libs.tasks import send_async_email


def welcome(email, **kwargs):
    message = {'email': email, 'subject': 'Flask Test Mail',
               'html': render_template('email/verification.html', **kwargs)}
    send_async_email.delay(message)
