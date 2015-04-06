# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=250, verbose_name="Card's Name")),
                ('description', models.TextField(verbose_name='Description')),
                ('life', models.PositiveIntegerField(default=0, verbose_name='Life')),
                ('damage', models.PositiveIntegerField(default=0, verbose_name='Damage')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CardType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=250, verbose_name='Type of Card')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='card',
            name='card_type',
            field=models.ForeignKey(verbose_name='Type of Card', to='cardsgame.CardType'),
            preserve_default=True,
        ),
    ]
