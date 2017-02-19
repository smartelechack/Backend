# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertransaction',
            name='transactionid',
            field=models.CharField(default=0, unique=True, max_length=256),
        ),
    ]
