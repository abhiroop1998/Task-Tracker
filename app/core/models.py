from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from app.user.managers import UserManager
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)

    # Additional field declarations
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # Set Django defaults
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # Unique identifier field - email instead if username
    USERNAME_FIELD = 'email'
    # Fields for superuser creation
    REQUIRED_FIELDS = ['password',]

    # Reference custom manager
    objects = UserManager()

    # String representation of model
    def __str__(self):
        return self.email


class TaskList(models.Model):
    title = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Task(models.Model):
    class Priority(models.TextChoices):
        LOW = 'low', _('Low')
        MEDIUM = 'medium', _('Medium')
        HIGH = 'high', _('High')

    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    priority = models.CharField(max_length=20, choices=Priority.choices, default=Priority.LOW)
    status = models.BooleanField(default=False)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
