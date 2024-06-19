from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.urls import path

from .views import (
    AccountCreateView,
    AccountDeleteView,
    AccountDetailView,
    AccountListView,
    AccountUpdateView,
    AccountLoginView,
    AccountLogoutView,
)

urlpatterns = [
    path('', AccountListView.as_view(), name='account-list'),
    path('create/', AccountCreateView.as_view(), name='account-create'),
    path('<int:account_id>/', AccountDetailView.as_view(), name='account-detail'),
    path('<int:account_id>/update/', AccountUpdateView.as_view(), name='account-update'),
    path('<int:account_id>/delete/', AccountDeleteView.as_view(), name='account-delete'),
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password-reset-done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password-reset-complete'),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
]
