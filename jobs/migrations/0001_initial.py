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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('tipo', models.CharField(choices=[('email', 'E-mail'), ('sms', 'SMS'), ('notificacao', 'Notificação Push')], max_length=10)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('titulo', models.CharField(max_length=100)),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='alarme',
            name='alarme',
            field=models.ForeignKey(to='jobs.Job'),
        ),
    ]
