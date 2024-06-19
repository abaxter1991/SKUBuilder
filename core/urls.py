from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from accounts.views import AccountLoginView
from sales.views import (
    SalesOrderListAPIView,
    SalesOrderCreateAPIView,
    SalesOrderUpdateAPIView,
    SalesOrderDestroyAPIView,
)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('api/sales_orders/list/', SalesOrderListAPIView.as_view(), name='sales_order_list_api'),
    path('api/sales_orders/create/', SalesOrderCreateAPIView.as_view(), name='sales_order_create_api'),
    path('api/sales_orders/update/', SalesOrderUpdateAPIView.as_view(), name='sales_order_update_api'),
    path('api/sales_orders/destroy/', SalesOrderDestroyAPIView.as_view(), name='sales_order_destroy_api'),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('admin/', admin.site.urls),
    path('', AccountLoginView.as_view()),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('integrations/', include('integrations.urls', namespace='integrations')),
    path('product_studio/', include('product_studio.urls', namespace='product_studio')),
    path('sales/', include('sales.urls', namespace='sales')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
