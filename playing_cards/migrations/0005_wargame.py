# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('playing_cards', '0004_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='WarGame',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result', models.IntegerField(choices=[(-1, b'loss'), (0, b'tie'), (1, b'win')])),
                ('player', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
