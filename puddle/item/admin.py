from django.contrib import admin

# Register your models here.

#importing category models

from .models import Category,Item

admin.site.register(Category)
admin.site.register(Item)
