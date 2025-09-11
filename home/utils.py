from django.core.mail import send_mail
from django.conf.global_settings import EMAIL_HOST_USER

def send_email_to_client():
    subject = "This is Test Mail"
    message = "Hi, this is test email sent for study purpose"
    from_email = EMAIL_HOST_USER
    recipient_list = ['chaudhari.ganesh33@gmail.com']
    send_mail(subject, message, from_email, recipient_list)