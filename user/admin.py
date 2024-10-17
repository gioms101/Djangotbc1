from django.contrib import admin
from .models import CustomUser


# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    filter_horizontal = ('groups', 'user_permissions',)
