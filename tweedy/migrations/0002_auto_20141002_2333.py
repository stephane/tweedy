# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweedy', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yield',
            old_name='by_user',
            new_name='user',
        ),
    ]
