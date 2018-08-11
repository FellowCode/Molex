from django.contrib import admin
from .models import Smartphone, CPUSmartphone, BrandSmartphone
from Products.admin import productInlines

@admin.register(CPUSmartphone)
class CPUSmartphoneAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

@admin.register(BrandSmartphone)
class BrandSmartphone(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


@admin.register(Smartphone)
class SmartphoneAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name', 'CPU')
    inlines = productInlines


