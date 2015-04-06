# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardsgame', '0002_card_mana_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='modified',
            field=models.PositiveIntegerField(null=True, verbose_name='Modified'),
            preserve_default=True,
        ),
    ]
