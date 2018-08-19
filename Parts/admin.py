from django.contrib import admin
from .models import *
from Products.admin import productInlines, ImageInline, ColorInline

@admin.register(GraphicCardBrand)
class GraphicCardBrandAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}
@admin.register(GPU)
class GPUAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}
@admin.register(GraphicCard)
class GraphicCardAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

@admin.register(GraphicCardProduct)
class GraphicCardAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


@admin.register(CPUSocket)
class CPUSocketAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}
@admin.register(CPU)
class CPUAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

@admin.register(CPUProduct)
class CPUAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

@admin.register(RAMBrand)
class RAMBrandAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

@admin.register(RAM)
class RAMAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
        ColorInline,
    ]


@admin.register(SSDBrand)
class SSDBrandAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}
@admin.register(SSD)
class SSDAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


@admin.register(InterfaceName)
class InterfaceNameAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}
@admin.register(MotherboardChipset)
class MotherboardChipsetAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}
@admin.register(MotherboardBrand)
class MotherboardBrandAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

class InterfaceInline(admin.TabularInline):
    model = MotherboardInterface


@admin.register(Motherboard)
class MotherboardAdmin(admin.ModelAdmin):
    inlines = [
        InterfaceInline,
        ImageInline,
    ]
