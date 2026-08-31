import os
import django
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.core import mail

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'altclan.settings')
django.setup()

User = get_user_model()

class DjoserPasswordResetTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.email = "testuser@example.com"
        self.user = User.objects.create_user(
            email=self.email, 
            password="TestPassword123!",
            first_name="Test",
            last_name="User"
        )
        
    def test_password_reset_email_format(self):
        # Trigger Djoser password reset
        response = self.client.post('/auth/users/reset_password/', {'email': self.email})
        self.assertEqual(response.status_code, 204)
        
        # Verify email was sent
        self.assertEqual(len(mail.outbox), 1)
        
        email_message = mail.outbox[0]
        
        # Check that the email body contains the correct domain and path
        self.assertIn('altclan.shop', email_message.body)
        self.assertIn('accounts/reset_password?uid=', email_message.body)
        
        print("\n--- TEST PASSED ---")
        print("Djoser correctly generated the reset link with the 'altclan.shop' domain and 'accounts/reset_password' path.")
        print("Generated Email Body:")
        print("--------------------")
        print(email_message.body)
        print("--------------------")

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage.py', 'test', 'test_djoser_reset', '--verbosity=2'])
