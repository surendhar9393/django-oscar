# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 08:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20170429_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='line',
            field=models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.PROTECT, to='order.OrderLine'),
        ),
        migrations.AlterUniqueTogether(
            name='productreview',
            unique_together=set([('product', 'user', 'line')]),
        ),
    ]
