# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-02 04:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0003_meal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500)),
                ('total', models.IntegerField()),
                ('status', models.IntegerField(choices=[(1, 'Cooking'), (2, 'Ready'), (3, 'On the way'), (4, 'Delivered')])),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('picked_at', models.DateTimeField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodtaskerapp.Customer')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodtaskerapp.Driver')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodtaskerapp.Restaurant')),
            ],
        ),
    ]
