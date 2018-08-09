from django.contrib import admin
from .models import Category, Image, Color, Option


admin.site.register(Category)

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



