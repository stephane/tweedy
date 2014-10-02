# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chicken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('begin', models.DateField(verbose_name='Date de d\xe9but')),
                ('end', models.DateField(null=True, verbose_name='Date de fin', blank=True)),
            ],
            options={
                'db_table': 'chicken',
                'verbose_name': 'Chicken',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Yield',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantit\xe9')),
                ('by_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('chicken', models.ForeignKey(verbose_name='Poule', blank=True, to='tweedy.Chicken', null=True)),
            ],
            options={
                'db_table': 'yield',
                'verbose_name': 'Production',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='yield',
            unique_together=set([('date', 'chicken')]),
        ),
    ]
