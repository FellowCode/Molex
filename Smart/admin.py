from django.contrib import admin
from .models import Smartphone, CPUSmartphone, BrandSmartphone
from Products.admin import productInlines


admin.site.register(CPUSmartphone)
admin.site.register(BrandSmartphone)

@admin.register(Smartphone)
class SmartphoneAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name', 'CPU')
    inlines = productInlines


