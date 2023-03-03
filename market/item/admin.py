from django.contrib import admin
from .models import Category, Item


class ItemAdmin(admin.ModelAdmin):
    list_display= ('category', 'name', 'price', 'is_sold', 'created_by', 'created_at')


# Register your models here.
admin.site.register(Category)
admin.site.register(Item, ItemAdmin)
