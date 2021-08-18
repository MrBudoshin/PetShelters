from django.contrib import admin
from .models import Pet, Profile


class PetAdmin(admin.ModelAdmin):
    model = Pet
    list_display = ['id', 'name', 'age', 'come_data', 'weight', 'special_signs']


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ['users', 'first_name', 'last_name', 'phone', 'mail']


admin.site.register(Pet, PetAdmin)
admin.site.register(Profile, ProfileAdmin)
