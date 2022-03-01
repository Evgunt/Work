from django.template.loader import render_to_string
from django.core.signing import Signer

from Ceramic.settings import ALLOWED_HOSTS

signer = Signer()


def send_password_notification(user):
    if ALLOWED_HOSTS:
        host = 'http://' + ALLOWED_HOSTS[0]
    else:
        host = 'http://localhost:8000'
    context = {'user': user, 'host': host, 'sign': signer.sign(user.username)}
    subject = "Восстановление пароля"
    body_text = render_to_string('email/password_letter_body.txt', context)
    user.email_user(subject, body_text)
