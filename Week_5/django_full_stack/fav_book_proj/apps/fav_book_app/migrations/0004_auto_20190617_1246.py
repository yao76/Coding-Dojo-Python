# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-17 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fav_book_app', '0003_remove_book_users_who_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='liked_book',
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='liked_by',
        ),
        migrations.AddField(
            model_name='book',
            name='users_who_like',
            field=models.ManyToManyField(related_name='liked_books', to='fav_book_app.User'),
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]