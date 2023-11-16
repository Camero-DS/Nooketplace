from django.contrib import admin
from .models import Productos
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["name","price","desc"]
    list_editable =["price","desc"]



admin.site.register(Productos, ProductoAdmin)