from django.core.management.base import BaseCommand
from faker import Faker

from accounts.models import Account
from core import settings


class Command(BaseCommand):
    help = 'Management command to create mock accounts to populate the database with testable data.'

    def add_arguments(self, parser):
        parser.add_argument('num_accounts', type=int)

    def handle(self, *args, **options):
        num_accounts = options['num_accounts']
        fake = Faker()
        Faker.seed(0)
        x = 0
        y = 0

        for index in range(num_accounts):
            # The profile pictures are named sequentially from profile_picture_0 to profile_picture_24.
            # To ensure we use these 25 images repeatedly, even if num_accounts is greater than 25,
            # we use the modulo operator to cycle through the picture numbers. The picture_num
            # variable will loop through 0 to 24 for each set of 25 accounts created.
            picture_num = index - (25 * (index // 25))

            try:
                media_base_path = ''

                if not settings.DEBUG:
                    media_base_path = 'media/'

                profile_picture_path = f'{media_base_path}images/profile_pictures/profile_picture_{picture_num}.png'

                first_name = fake.first_name()
                last_name = fake.last_name()
                username = f'{first_name}{last_name}'.lower()
                email_address = f'{username}@example.com'
                password = '1234'
                profile_picture = profile_picture_path
                is_active = fake.boolean(chance_of_getting_true=95)
                is_staff = fake.boolean(chance_of_getting_true=50)
                is_admin = fake.boolean(chance_of_getting_true=5)
                is_superuser = fake.boolean(chance_of_getting_true=5)

                if is_superuser:
                    is_active = True
                    is_staff = True
                    is_admin = True
                    new_user = Account.objects.create_superuser
                else:
                    new_user = Account.objects.create_user

                new_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email_address=email_address,
                    password=password,
                    profile_picture=profile_picture,
                    is_active=is_active,
                    is_staff=is_staff,
                    is_admin=is_admin,
                    is_superuser=is_superuser)

                x += 1

            except Exception as error:
                y += 1
                print(error)

        print(f'{x}/{num_accounts} accounts were created.')
