# -*- coding: utf-8 -*-
from djando.models import Film, Actor, Director
from django.views.generic import ListView, DetailView
from django.shortcuts import render

class MainView(ListView):
    model = Film
    main_film = Film.objects.order_by('-date_publication')[:5]
    template_name = 'main.html'
    context_object_name = 'main_films'

class NoveltyView(ListView):
    model = Film
    novelty_films = Film.objects.order_by('-date_publication')
    template_name = 'novelty.html'
    context_object_name = 'novelty_films'

class FilmView(DetailView):
    model = Film
    template_name = 'film.html'
    context_object_name = 'films'

class ActorView(DetailView):
    model = Actor
    template_name = 'actor.html'
    context_object_name = 'actor'

class DirectorView(DetailView):
    model = Director
    template_name = 'director.html'
    context_object_name = 'director'

