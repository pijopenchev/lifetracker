# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lifetracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='note',
            table='note',
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
