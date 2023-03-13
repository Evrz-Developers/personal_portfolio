from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    # define custom admin behavior here
    fieldsets = UserAdmin.fieldsets
    fieldsets[1][1]['fields'] += ('profile_picture', 'resume', 'contact')


admin.site.register(CustomUser, CustomUserAdmin)
