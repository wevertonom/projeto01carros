from django.contrib import admin
from .models import Car , Brand

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('Model', 'Brand', 'FactoryYear', 'ModelYear','Value','Place','Photo','id')
    search_fields = ('Model',)

class CarBrand(admin.ModelAdmin):
    list_display = ('Name','id')
    search_fields = ('Name',)

admin.site.register(Car, CarAdmin )
admin.site.register(Brand, CarBrand )