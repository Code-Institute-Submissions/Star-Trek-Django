# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-09 12:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0012_auto_20200404_1022'),
        ('news', '0004_auto_20200405_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='tag',
            field=models.CharField(choices=[('N', 'News'), ('F', 'FNN')], max_length=1),
        ),
        migrations.AddField(
            model_name='newscomment',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='newscomment', to='news.News'),
        ),
        migrations.AddField(
            model_name='newscomment',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile'),
        ),
        migrations.AddField(
            model_name='newscomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
