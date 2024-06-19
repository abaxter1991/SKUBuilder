from django.urls import path

from . import views

app_name = 'integrations'

urlpatterns = [
    path('', views.integrations, name='integrations'),
]
