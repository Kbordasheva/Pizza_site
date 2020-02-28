from django.contrib import admin
from .models import *


class PizzaProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PizzaProduct._meta.fields]

    class Meta:
        Model = PizzaProduct


admin.site.register(PizzaProduct, PizzaProductAdmin)