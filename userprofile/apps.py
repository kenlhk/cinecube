
from django.apps import AppConfig
from userprofile.models import User
from django.contrib import admin


class UserprofileConfig(AppConfig):
    name = 'userprofile'

admin.site.register(User)

