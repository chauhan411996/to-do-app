from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

class Todo(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField()
    category = models.CharField(max_length=50)
    due_date = models.DateField()
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)