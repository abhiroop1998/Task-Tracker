from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.

    """

    def create_user(self, email, password, **extra_fields):
        """ Create and save a new user """

        user = self.model(email=email, **extra_fields)
        # Set password with hash
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password, **extra_fields):
        """ Create and save a new superuser """

        user = self.create_user(phone, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
