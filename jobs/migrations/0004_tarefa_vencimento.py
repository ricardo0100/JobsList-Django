# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20150525_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='vencimento',
            field=models.DateTimeField(null=True),
        ),
    ]
