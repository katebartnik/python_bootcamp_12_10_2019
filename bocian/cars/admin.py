from django.contrib import admin

# Register your models here.
from cars.models import Car, Engine


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass

@admin.register(Engine)
class EngineAdmin(admin.ModelAdmin):
    pass
