from django.contrib import admin
from .models import Producto, Cerveza


# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass

@admin.register(Cerveza)
class CervezaAdmin(admin.ModelAdmin):
    pass
