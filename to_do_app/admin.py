from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Todo

admin.site.register(CustomUser)
admin.site.register(Todo)