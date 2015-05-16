import datetime
from django.db import models

class ModelBase(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        return super(ModelBase, self).save(*args, **kwargs)


class Job(ModelBase):
    titulo = models.CharField(max_length=100)
    alarme = models

    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()


class Alarme(ModelBase):
    TIPOS_ALARME = (
        ('email', 'E-mail'),
        ('sms', 'SMS'),
        ('notificacao', 'Notificação Push'),
    )
    tipo = models.CharField(choices=TIPOS_ALARME, max_length=10)
    alarme = models.ForeignKey(Job)
    horario = models.DateTimeField()
    ativo = models.BooleanField()
