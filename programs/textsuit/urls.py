from django.urls import path
from . import views

urlpatterns = [
    path('', views.textsuit_home, name='textsuit_home')
]
