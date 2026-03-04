from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Address, Profile

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'is_seller', 'is_staff']
    list_filter = ['is_seller', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('phone', 'is_seller')}),
    )

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'city', 'is_default']
    list_filter = ['is_default', 'country']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth']
