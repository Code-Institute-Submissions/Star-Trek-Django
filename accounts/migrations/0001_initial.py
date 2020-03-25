# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-25 14:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pic')),
                ('name', models.CharField(max_length=40)),
                ('bio', models.TextField(max_length=500)),
                ('password', models.CharField(max_length=40)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='uprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
