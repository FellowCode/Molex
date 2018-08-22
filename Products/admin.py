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
    readonly_fields = ('goods', 'person_pay', 'payment_amount', 'person_name', 'person_phone', 'person_email',
                       'payment_method', 'person_payment_account', 'payment_datetime', 'payment_operation_id',
                       'payment_status', 'datetime')

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



