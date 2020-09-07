from django.contrib import admin
from django.urls import path, include

from bot import views

urlpatterns = [
    path('event/', views.event, name="event"),
    path('response/(?P<response+)/$', views.res, name="res"),
    path('teste/', views.teste, name="teste"),

]
