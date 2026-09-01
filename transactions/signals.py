from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Order
from ..core.email_utils import send_notification

@receiver(post_save, sender=Order)
def order_created(sender, instance, created, **kwargs):
    if created:
        subject = 'Your Altclan Order Confirmation'
        base_url = getattr(settings, 'FRONTEND_BASE_URL', '')
        order_link = f"{base_url}/orders/{instance.id}" if base_url else ''
        message = f"Thank you for your order!\n\nTracking Number: {instance.tracking_number}\nOrder ID: {instance.id}\n"
        if order_link:
            message += f"View your order details: {order_link}\n"
        recipient_list = [instance.user_email]
        # Build HTML version of the email
        html_message = f"""
        <html><body>
        <h2>Your Altclan Order Confirmation</h2>
        <p>Thank you for your order!</p>
        <p><strong>Tracking Number:</strong> {instance.tracking_number}<br/>
        <strong>Order ID:</strong> {instance.id}</p>
        {f'<p>View your order details: <a href="{order_link}">{order_link}</a></p>' if order_link else ''}
        </body></html>
        """
        plain_text = f"Thank you for your order!\nTracking Number: {instance.tracking_number}\nOrder ID: {instance.id}\n"
        if order_link:
            plain_text += f"View your order details: {order_link}\n"
        send_notification(subject, plain_text, recipient_list, html_message=html_message)
