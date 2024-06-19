from django.urls import path

from . import views

app_name = 'sales'

urlpatterns = [
    path('', views.sales, name='sales'),
    path('faire/', views.faire_api, name='faire'),
]
