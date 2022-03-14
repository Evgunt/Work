from string import ascii_letters, digits
from random import sample
from django.core.signing import Signer

from Ceramic.settings import ALLOWED_HOSTS, DEFAULT_FROM_EMAIL
from post_office import mail

signer = Signer()


def generate_password():
    letters_and_digits = ascii_letters + digits
    rand_string = ''.join(sample(letters_and_digits, 9))
    return rand_string


def send_password_notification(user):
    if ALLOWED_HOSTS:
        host = 'https://' + ALLOWED_HOSTS[0]
    else:
        host = 'http://127.0.0.1:8000'
    mail.send(
        user.email,
        DEFAULT_FROM_EMAIL,
        template='send_password_notification',
        context={'user': user, 'host': host, 'sign': signer.sign(user.username)},
        priority='now',
    )

#
# def send_help_notification(mails):
#     subject = "Вопрос к службе поддержки"
#     # user.email_user(subject, body_text, from_email='')
#     mail.send(
#         EMAIL_HOST_USER,
#         mails.email,
#         subject=subject,
#         context=mails.question)
