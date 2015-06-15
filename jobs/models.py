import datetime
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import models
from django.db.models import Q
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


class Grupo(ModelBase):
    def __str__(self):
        return self.nome

    nome = models.CharField(max_length=100)

    @property
    def quantidade_pendentes(self):
        filtro = Q(Q(concluida=False) | Q(vencimento__lt=timezone.now(), concluida=False))
        filtro &= Q(grupo=self)

        count = Tarefa.objects.filter(filtro).count()

        return count


class Tarefa(ModelBase):
    def __str__(self):
        return self.titulo

    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    vencimento = models.DateTimeField(null=True)
    concluida = models.BooleanField(default=False)

    grupo = models.ForeignKey(Grupo, null=True)

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
