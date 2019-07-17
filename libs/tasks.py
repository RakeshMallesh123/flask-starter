import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from celery_background import celery


@celery.task
def send_async_email(data):
    if os.environ.get("SEND_EMAIL"):
        message = Mail(
            from_email=os.environ.get('SENDGRID_DEFAULT_FROM'),
            to_emails=data['email'],
            subject=data['subject'],
            html_content=data['html'])
        try:
            sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sendgrid_client.send(message)
            print('Email sent')
            return True
        except Exception as e:
            print(e)
    else:
        print("Email sending is disabled")
