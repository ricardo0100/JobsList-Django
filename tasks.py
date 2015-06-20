from django.core.mail import send_mail
from celery import Celery
from main.settings import RABBITMQ_BIGWIG_RX_URL

app = Celery('tasks', broker=RABBITMQ_BIGWIG_RX_URL)

@app.task
def enviar_alarme_por_email(destinatario, assunto, mensagem):
    send_mail(assunto, mensagem, 'ricardo0100@gmail.com', ['ricardo0100@gmail.com'], fail_silently=False)
