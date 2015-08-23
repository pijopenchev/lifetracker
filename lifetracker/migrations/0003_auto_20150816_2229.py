# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lifetracker', '0002_auto_20150816_2226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='user_id',
            new_name='user',
        ),
    ]
