from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email_contact_us(subject, message, from_email, email_host_user):
    recipient_list = [email_host_user]

    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list
    )
