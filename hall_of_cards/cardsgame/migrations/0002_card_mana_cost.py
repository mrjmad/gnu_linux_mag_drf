# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardsgame', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='mana_cost',
            field=models.PositiveIntegerField(default=0, verbose_name='Mana Cost'),
            preserve_default=True,
        ),
    ]
