from django.core.management.base import BaseCommand

from accounts.models import Account
from core import settings


class Command(BaseCommand):
    help = 'Management command to create 1 superuser.'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        media_base_path = ''

        if not settings.DEBUG:
            media_base_path = 'media/'

        profile_picture_path = f'{media_base_path}images/profile_pictures/profile_picture_0'

        first_name = 'Austin'
        last_name = 'Baxter'
        username = 'abaxter1991'
        email_address = 'abaxter1991@gmail.com'
        password = '1234'
        profile_picture = profile_picture_path
        is_active = True
        is_staff = True
        is_admin = True
        is_superuser = True

        Account.objects.create_superuser(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email_address=email_address,
            password=password,
            profile_picture=profile_picture,
            is_active=is_active,
            is_staff=is_staff,
            is_admin=is_admin,
            is_superuser=is_superuser,
        )
