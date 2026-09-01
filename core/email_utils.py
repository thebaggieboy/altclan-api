from django.conf import settings
from django.core.mail import EmailMultiAlternatives

def send_notification(subject: str, message: str, recipient_list: list[str], html_message: str | None = None):
    """Send an email using Django's email backend (AnyMail Resend).

    Parameters:
        subject: Email subject.
        message: Plain‑text fallback content.
        recipient_list: List of recipient email addresses.
        html_message: Optional HTML version of the email. If omitted the plain
            text ``message`` is sent.
    """
    if html_message:
        email = EmailMultiAlternatives(
            subject=subject,
            body=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=recipient_list,
        )
        email.attach_alternative(html_message, "text/html")
        email.send(fail_silently=False)
    else:
        # Fallback to simple send_mail if no HTML provided
        from django.core.mail import send_mail
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=recipient_list,
            fail_silently=False,
        )








