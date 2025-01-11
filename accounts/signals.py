
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from .models import Profile
 
from .models import AccountUser
 
from brands.models import UserBillingAddress, BillingAddress
from django.core.mail import send_mail


subject = 'Welcome to Altclan: Our community of Aesthetics'
message = """
Dear [User's Name],

Welcome to Altclan! We’re thrilled to have you join our vibrant community of fashion enthusiasts and aesthetes.
At Altclan, we strive to bring you the latest trends and unique pieces that elevate your style and express your individuality. 
Whether you’re looking for the latest fashion, exclusive designs, or aesthetic inspirations, we’ve got you covered.

To get started, here are a few things you can do:
Explore Our Collections: Discover a curated selection of fashion items and aesthetic pieces tailored to your taste.
Personalize Your Profile: Complete your profile to receive personalized recommendations and exclusive offers.
Join the Conversation: Connect with other members of the Altclan community to share your style tips, inspirations, and feedback.
We’re here to support you every step of the way. If you have any questions or need assistance, feel free to reach out to our support team at [support email/contact info].

Thank you for choosing Altclan. We look forward to being a part of your fashion journey!

Best regards,

Enimofe Odujirin
Founder, Altclan
[https://altclan.store]
[noreply@altclan.store]
"""
email_from = 'noreply@altclan.store'
recipient_list = ['baggieboy702@gmail.com']

User = settings.AUTH_USER_MODEL
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        
        Profile.objects.create(user=instance)
        print("New user profile has been created for ", instance.email)
        # send email to new user
        #send_mail( subject, message, email_from, recipient_list )


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    print("Profile saved!")
   
 

