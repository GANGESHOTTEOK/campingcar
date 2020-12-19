from django.contrib import admin
from .models import Car, Option, Company, Tax
# Register your models here.

class OptionInline(admin.StackedInline):
    model = Option.car.through

class CarAdmin(admin.ModelAdmin):
    inlines = [
    	OptionInline,
    ]

admin.site.register(Car, CarAdmin)
admin.site.register(Option)
admin.site.register(Company)
admin.site.register(Tax)
