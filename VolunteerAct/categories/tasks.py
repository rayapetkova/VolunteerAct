from celery import shared_task
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from VolunteerAct.categories.models import Category, Event
from VolunteerAct.categories.utils import get_active_members_for_category


AppUser = get_user_model()


@shared_task
def send_email_to_active_members_in_this_category(category_id, user_id, event_id):
    category = Category.objects.filter(id=category_id).first()
    user = AppUser.objects.get(id=user_id)
    event = Event.objects.filter(id=event_id).first()

    active_members = get_active_members_for_category(category)
    emails = [member.email for member in active_members if member.email != user.email]

    email_context = {
        'event_title': event.title,
        'event_time': event.time,
        'category_name': category.name,
        'event_exact_location': event.exact_location(),
        'host_email': event.host.email
    }

    subject = f"🚨 Urgent Alert: Emergency Event in {category.name}!"
    recipient_list = emails
    template_name = 'emails/emergency_event.html'
    convert_to_html_content = render_to_string(
        template_name=template_name,
        context=email_context
    )
    plain_message = strip_tags(convert_to_html_content)

    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipient_list,
        html_message=convert_to_html_content,
        fail_silently=True
    )