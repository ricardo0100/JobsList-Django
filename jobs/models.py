import datetime
from django.contrib.auth.models import User
from django.db import models

class ModelBase(models.Model):
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    usuario = models.ForeignKey(User)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        return super(ModelBase, self).save(*args, **kwargs)


class Tarefa(ModelBase):
    def __str__(self):
        return self.titulo

    titulo = models.CharField(max_length=100)
    descricao = models.TextField()


class Alarme(ModelBase):
    TIPOS_ALARME = (
        ('email', 'E-mail'),
        ('sms', 'SMS'),
        ('notificacao', 'Notificação Push'),
    )
    tipo = models.CharField(choices=TIPOS_ALARME, max_length=10)
    job = models.ForeignKey(Tarefa)
    horario = models.DateTimeField()
    ativo = models.BooleanField()
