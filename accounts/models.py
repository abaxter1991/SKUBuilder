from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.urls import reverse

from .managers import UserAccountManager


class Account(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50, blank=True, verbose_name='First Name')
    last_name = models.CharField(max_length=50, blank=True, verbose_name='Last Name')
    username = models.CharField(max_length=50, unique=True, verbose_name='Username')
    email_address = models.EmailField(unique=True, verbose_name='Email Address')
    is_active = models.BooleanField(default=True, verbose_name='Active')
    is_staff = models.BooleanField(default=False, verbose_name='Staff')
    is_admin = models.BooleanField(default=False, verbose_name='Admin')
    is_superuser = models.BooleanField(default=False, verbose_name='Superuser')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')
    last_login = models.DateTimeField(auto_now=True, verbose_name='Last Login')
    profile_picture = models.ImageField(
        default='media/images/profile_pictures/default.png',
        upload_to='media/images/profile_pictures',
    )

    objects = UserAccountManager()

    USERNAME_FIELD = 'email_address'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        db_table = 'account'

    def __str__(self):
        return self.username

    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'

        return full_name.strip()

    def get_absolute_url(self):
        return reverse('accounts:user_detail', kwargs={'id': self.id})
