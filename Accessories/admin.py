from django.contrib import admin
from .models import Mousepad
from Products.admin import productInlines


@admin.register(Mousepad)
class MousepadAdmin(admin.ModelAdmin):
    inlines = productInlines