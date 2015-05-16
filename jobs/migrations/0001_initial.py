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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField()),
                ('tipo', models.CharField(max_length=10, choices=[('email', 'E-mail'), ('sms', 'SMS'), ('notificacao', 'Notificação Push')])),
                ('horario', models.DateTimeField()),
                ('ativo', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
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
            field=models.ForeignKey(to='jobs.Job'),
        ),
    ]
