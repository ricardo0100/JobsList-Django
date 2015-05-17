# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alarme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField()),
                ('tipo', models.CharField(choices=[('email', 'E-mail'), ('sms', 'SMS'), ('notificacao', 'Notificação Push')], max_length=10)),
                ('horario', models.DateTimeField()),
                ('ativo', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField()),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='alarme',
            name='job',
            field=models.ForeignKey(to='jobs.Tarefa'),
        ),
    ]
