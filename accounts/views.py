from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from .forms import AccountCreateModelForm
from .models import Account


class AccountListView(LoginRequiredMixin, ListView):
    template_name = 'accounts/account-list.html'
    context_object_name = 'accounts'
    model = Account

    def get_queryset(self, *args, **kwargs):
        queryset = Account.objects.all()

        return queryset


class AccountCreateView(LoginRequiredMixin, CreateView):
    template_name = 'accounts/account-create.html'
    form_class = AccountCreateModelForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accounts:account-list')


class AccountDetailView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/account-detail.html'
    context_object_name = 'account'
    model = Account

    def get_object(self):
        account_id = self.kwargs.get('account_id')

        return Account.objects.get(id=account_id)


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/account-create.html'
    form_class = AccountCreateModelForm

    def get_object(self):
        account_id = self.kwargs.get('account_id')
        obj = Account.objects.get(id=account_id)

        return obj

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accounts:account-list')


class AccountDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'accounts/account-delete.html'

    def get_queryset(self):
        account_id = self.kwargs.get('account_id')

        return Account.objects.filter(id=account_id)

    def get_success_url(self):
        return reverse('accounts:account-list')


class AccountLoginView(LoginView):
    redirect_authenticated_user = True


class AccountLogoutView(LogoutView):
    # TODO: this class is not needed due to adding a logout redirect variable in settings file, but will leave here
    #       for future expandability.
    next_page = None # '/accounts/login'
