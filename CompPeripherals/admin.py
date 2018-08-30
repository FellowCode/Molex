from django.contrib import admin
from .models import MouseBrand, Mouse, KeyboardBrand, Keyboard, HeadphoneBrand, Headphone, Speaker, SpeakerBrand, SpeakerInterface, SpeakerInterfaceName, SpeakerFrequencyDiapason
from Products.admin import productInlines, ImageInline, ColorInline


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

@admin.register(SpeakerBrand)
class SpeakerBrandAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

@admin.register(SpeakerFrequencyDiapason)
class SpeakerFrequencyDiapason(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

@admin.register(SpeakerInterfaceName)
class SpeakerInterfaceNameAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

class SpeakerInterfaceInline(admin.TabularInline):
    model = SpeakerInterface
    extra = 0

@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
        SpeakerInterfaceInline,
        ColorInline
    ]

