from django.conf.urls import include, url
from .views import MyBotView
from mybot import views
urlpatterns = [
    url(r'^callback/?$', MyBotView.as_view()),
    url(r'^index/', views.index, name='index'),
]
