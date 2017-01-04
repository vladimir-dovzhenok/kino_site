# -*- coding: utf-8 -*-
from django.db import models

class Film(models.Model):
    actors = models.ManyToManyField('Actor')
    directors = models.ManyToManyField('Director')
    name = models.CharField(max_length=50, verbose_name=u'Название')
    genre = models.CharField(max_length=40, verbose_name=u'Жанр')
    state = models.CharField(max_length=30, verbose_name=u'Старана')
    file = models.FileField()

class Information(models.Model):
    first_name = models.CharField(max_length=30, verbose_name=u'Имя')
    last_name = models.CharField(max_length=30, verbose_name=u'Фамилия')
    age = models.IntegerField(verbose_name=u'Возраст')
    state = models.CharField(max_length=30, verbose_name=u'Страна')
    image = models.ImageField(verbose_name=u'Изображение')
    biography = models.TextField(verbose_name=u'Биография')

    class Meta:
        abstract = True
        ordering = ['last_name']

class Actor(Information):
    actor_film = models.ManyToManyField('Film')

class Director(Information):
    director_film = models.ManyToManyField('Film')




