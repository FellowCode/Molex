from django.contrib import admin
from .models import GraphicCardProduct, GPU, GraphicCardBrand, CPUProduct, CPUSocket, RAM, Motherboard, SSD, \
    MotherboardBrand, SSDBrand, MotherboardInterface, MotherboardChipset, InterfaceName, CPU, GraphicCard
from Products.admin import productInlines, ImageInline

admin.site.register(GraphicCardBrand)
admin.site.register(GPU)
admin.site.register(GraphicCard)
@admin.register(GraphicCardProduct)
class GraphicCardAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(CPUSocket)
admin.site.register(CPU)
@admin.register(CPUProduct)
class CPUAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(RAM)

admin.site.register(SSDBrand)
admin.site.register(SSD)

admin.site.register(InterfaceName)
admin.site.register(MotherboardChipset)
admin.site.register(MotherboardBrand)
class InterfaceInline(admin.TabularInline):
    model = MotherboardInterface
@admin.register(Motherboard)
class MotherboardAdmin(admin.ModelAdmin):
    inlines = [
        InterfaceInline,
        ImageInline,
    ]
