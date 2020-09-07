from django.contrib import admin
from django.urls import path, include

from bot import views

urlpatterns = [
    path('event/', views.event, name="event"),
    path('teste/', views.teste, name="teste"),

]
