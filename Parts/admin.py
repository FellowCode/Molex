from django.contrib import admin
from .models import GraphicCard, GPU, GraphicCardBrand, CPU, CPUsocket, RAM
from Products.admin import productInlines

admin.site.register(GraphicCardBrand)
admin.site.register(GPU)

@admin.register(GraphicCard)
class GraphicCardAdmin(admin.ModelAdmin):
    inlines = productInlines

admin.site.register(CPUsocket)
admin.site.register(CPU)

admin.site.register(RAM)
