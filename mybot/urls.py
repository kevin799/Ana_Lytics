# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from .views import MyBotView
from mybot import views
urlpatterns = [
    url(r'^callback/?$', MyBotView.as_view()),
    #url(r'^index/', views.index, name='index'),
    url(r'^$', views.bot_on, name='index'),
    url(r'^/imagem/', views.imagem, name='imagem'),
]
