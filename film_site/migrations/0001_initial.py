# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-04 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('state', models.CharField(max_length=30, verbose_name='Страна')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('biography', models.TextField(verbose_name='Биография')),
            ],
            options={
                'abstract': False,
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('state', models.CharField(max_length=30, verbose_name='Страна')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('biography', models.TextField(verbose_name='Биография')),
            ],
            options={
                'abstract': False,
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('genre', models.CharField(max_length=40, verbose_name='Жанр')),
                ('state', models.CharField(max_length=30, verbose_name='Старана')),
                ('file', models.FileField(upload_to='')),
                ('actors', models.ManyToManyField(to='film_site.Actor')),
                ('directors', models.ManyToManyField(to='film_site.Director')),
            ],
        ),
        migrations.AddField(
            model_name='director',
            name='director_film',
            field=models.ManyToManyField(to='film_site.Film'),
        ),
        migrations.AddField(
            model_name='actor',
            name='actor_film',
            field=models.ManyToManyField(to='film_site.Film'),
        ),
    ]
