# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 18:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0006_entity_relationship_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllEntityProxy',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('entity.entity',),
        ),
    ]