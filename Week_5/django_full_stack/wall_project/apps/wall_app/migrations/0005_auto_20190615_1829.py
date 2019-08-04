# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-16 01:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall_app', '0004_auto_20190615_1755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='user',
            new_name='posted_by',
        ),
        migrations.RemoveField(
            model_name='message',
            name='user_messsage',
        ),
        migrations.AddField(
            model_name='message',
            name='message_content',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]