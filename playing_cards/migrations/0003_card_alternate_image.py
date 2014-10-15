# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playing_cards', '0002_card_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='alternate_image',
            field=models.ImageField(null=True, upload_to=b'alt_images', blank=True),
            preserve_default=True,
        ),
    ]
