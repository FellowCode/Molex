from django.contrib import admin
from .models import CarouselImage, ServiceOrder, Budget

admin.site.register(CarouselImage)

@admin.register(ServiceOrder)
class ServiceOrderAdmin(admin.ModelAdmin):
    readonly_fields = ['service_type', 'email', 'name', 'phone', 'note']

admin.site.register(Budget)
