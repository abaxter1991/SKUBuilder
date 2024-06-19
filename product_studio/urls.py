from django.urls import path

from . import views

app_name = 'product_studio'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_studio'),
    path('create/', views.ProductCreateView.as_view(), name='product_create'),
    path('smart_reorder/', views.ProductPartSmartReorder.as_view(), name='smart_reorder'),
]
