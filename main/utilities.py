from django.template.loader import render_to_string
from django.core.signing import Signer

from Ceramic.settings import ALLOWED_HOSTS, EMAIL_HOST_USER
from post_office import mail
signer = Signer()


def send_password_notification(user):
    if ALLOWED_HOSTS:
        host = 'https://' + ALLOWED_HOSTS[0]
    else:
        host = 'http://localhost:8000'
    context = {'user': user, 'host': host, 'sign': signer.sign(user.username)}
    subject = "Восстановление пароля"
    body_text = render_to_string('email/password_letter_body.txt', context)
    # user.email_user(subject, body_text, from_email='')
    mail.send(
        user.email,
        EMAIL_HOST_USER,
        subject=subject,
        context=body_text)


def send_help_notification(mails):
    subject = "Вопрос к службе поддержки"
    # user.email_user(subject, body_text, from_email='')
    mail.send(
        EMAIL_HOST_USER,
        mails.email,
        subject=subject,
        context=mails.question)
