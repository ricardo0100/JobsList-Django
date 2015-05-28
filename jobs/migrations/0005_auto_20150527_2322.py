# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_tarefa_vencimento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alarme',
            old_name='job',
            new_name='tarefa',
        ),
        migrations.AddField(
            model_name='tarefa',
            name='concluida',
            field=models.BooleanField(default=False),
        ),
    ]
