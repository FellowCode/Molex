from django.contrib import admin
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ('parent', 'name')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class ColorInline(admin.TabularInline):
    model = Color
    extra = 1

class OptionInline(admin.TabularInline):
    model = Option
    extra = 1

productInlines = [
    ImageInline,
    ColorInline,
    OptionInline,
]



