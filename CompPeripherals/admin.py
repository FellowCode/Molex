from django.contrib import admin
from .models import MouseBrand, Mouse, KeyboardBrand, Keyboard, HeadphoneBrand, Headphone, Mousepad
from Products.admin import productInlines

@admin.register(Mousepad)
class MousepadAdmin(admin.ModelAdmin):
    inlines = productInlines

@admin.register(MouseBrand)
class MouseBrandAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

@admin.register(Mouse)
class MouseAdmin(admin.ModelAdmin):
    inlines = productInlines


@admin.register(KeyboardBrand)
class KeyboardBrandAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

@admin.register(Keyboard)
class KeyboardAdmin(admin.ModelAdmin):
    inlines = productInlines


@admin.register(HeadphoneBrand)
class HeadphoneBrandAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

@admin.register(Headphone)
class HeadphoneAdmin(admin.ModelAdmin):
    inlines = productInlines