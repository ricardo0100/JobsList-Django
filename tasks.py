from django.core.mail import send_mail
from celery import Celery

app = Celery('tasks', broker='amqp://guest@localhost//')

@app.task
def enviar_alarme_por_email(destinatario, assunto, mensagem):
    print(destinatario)
    send_mail(assunto, mensagem, 'ricardo0100@gmail.com', ['ricardo0100@gmail.com'], fail_silently=False)
