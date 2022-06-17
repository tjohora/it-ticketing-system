from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('ticket', views.create_ticket, name='create_ticket'),
]