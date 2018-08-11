from Products.admin import productInlines
from .models import Computer
from django.contrib import admin


@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    inlines = productInlines

