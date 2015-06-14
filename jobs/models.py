import datetime
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone


class ModelBase(models.Model):
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    usuario = models.ForeignKey(User)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(ModelBase, self).save(*args, **kwargs)


class Tarefa(ModelBase):
    def __str__(self):
        return self.titulo

    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    vencimento = models.DateTimeField(null=True)
    concluida = models.BooleanField(default=False)

    @property
    def vencida(self):
        return self.vencimento < timezone.now()

    @property
    def exibir_como_vencida(self):
        return self.vencida and not self.concluida


class Alarme(ModelBase):
    TIPOS_ALARME = (
        ('email', 'E-mail'),
        ('sms', 'SMS'),
        ('notificacao', 'Notificação Push'),
    )
    tipo = models.CharField(choices=TIPOS_ALARME, max_length=10)
    tarefa = models.ForeignKey(Tarefa)
    horario = models.DateTimeField()
    ativo = models.BooleanField()
