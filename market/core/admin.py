from django.contrib import admin
from .models import ContactProfile

# Register your models here.
@admin.register(ContactProfile)
class ContactProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')