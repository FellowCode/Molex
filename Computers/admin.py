from Products.admin import productInlines
from .models import Computer, CPU, GPU
from django.contrib import admin

admin.site.register(CPU)
admin.site.register(GPU)

@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    inlines = productInlines

