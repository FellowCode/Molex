from Products.admin import ImageInline, OptionInline, ColorInline
from .models import Computer, ComputerInterface, InterfaceName, Laptop, LaptopCPU, LaptopBrand, LaptopInterface, LaptopGPU, LaptopIntegralGPU
from django.contrib import admin

@admin.register(InterfaceName)
class InterfaceNameAdmin(admin.ModelAdmin):
    pass

class CompInterfaceInline(admin.TabularInline):
    model = ComputerInterface

@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    inlines = [
        CompInterfaceInline,
        ImageInline,
        OptionInline,
    ]

@admin.register(LaptopCPU)
class LaptopCPUAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

@admin.register(LaptopBrand)
class LaptopBrandAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

@admin.register(LaptopIntegralGPU)
class LaptopIntegralGPUAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

@admin.register(LaptopGPU)
class LaptopGPUAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

@admin.register(LaptopInterface)
class LaptopInterfaceAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

class LaptopInterfaceInline(admin.TabularInline):
    model = LaptopInterface
    extra = 0

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    inlines = [
        LaptopInterfaceInline,
        ImageInline,
        ColorInline,
        OptionInline,
    ]