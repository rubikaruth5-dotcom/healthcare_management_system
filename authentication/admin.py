from django.contrib import admin
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.admin import TokenAdmin


if not admin.site.is_registered(Token):
    admin.site.register(Token, TokenAdmin)