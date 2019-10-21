# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from .views import MyBotView
from mybot import views
urlpatterns = [
    url(r'^callback/?$', MyBotView.as_view()),
    #url(r'^index/', views.index, name='index'),
    url(r'^$', views.bot_on, name='index'),
    url(r'^/imagem/', views.imagem, name='imagem'),
    url(r'^/acao/', views.acao_inter, name='acao'),
    url(r'^/painelBordo/', views.sas_print, name='sas'),
    url(r'^/painelExecutivo/', views.painelExecutivo_print, name='painelExecutivo'),
    url(r'^/pdd/', views.pdd_print, name='pdd'),
    url(r'^/fpd/', views.fpd_print, name='fpd'),
    url(r'^/ipf/', views.ipf_print, name='ipf'),

]
