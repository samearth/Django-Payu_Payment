# Django-Payu_Payment
This is a web-app for Integration of payu money Gateway with Django 3.0 using Paywix

1. Go to master branch and clone to directly install it in your django project ready to use.

How to Use->

1. Create Merchant account on Payu Money
2. Copy Merchant Key and Salt Id .
3. Paste This in your Settings
PAYU_CONFIG = {
    "merchant_key": "******",
    "merchant_salt": "******",
    "mode": "test",
    "success_url": "http://127.0.0.1:8000/success", // Your URL to redirect after a successful transaction
    "failure_url": "http://127.0.0.1:8000/failure"  // Similar
}
  
4.Run pip install paywix

5. Add this app and paywix to your settings.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'payment(this app name)'
    'paywix',
]

6. Do not Change Paydem Template.

7. Change the Home, Success and failure Templates according to your Needs.

// You're Done
