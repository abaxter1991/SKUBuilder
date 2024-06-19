from django.contrib.auth.models import BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email_address, password, **extra_fields):
        if not email_address:
            raise ValueError('You must provide an email address')

        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_admin', False)
        extra_fields.setdefault('is_superuser', False)

        email_address = self.normalize_email(email_address)

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email_address=email_address,
            **extra_fields,
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, first_name, last_name, username, email_address, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')

        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must be assigned to is_admin=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        return self.create_user(first_name, last_name, username, email_address, password, **extra_fields)