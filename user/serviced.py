from django.contrib.auth.models import User
from django.core.mail import EmailMessage


def mailing(username):
    email_list = []
    obj = User.objects.filter(is_superuser=True)
    for user in obj:
        email_list.append(user.email)
    subjects = 'hi'
    body = f'User with {username} register in database, pls check him !'
    email = EmailMessage(subject=subjects, body=body, to=email_list)
    email.send()


def validate_password(password):
    if len(password) >= 8 and  password.isdigit() and  password.isalpha():
        return True
    else:
        return False
