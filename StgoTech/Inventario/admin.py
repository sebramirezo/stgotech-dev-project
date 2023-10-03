from django.contrib import admin
from .models import *

class BodegaAdmin(admin.ModelAdmin):
    search_fields = ('name_bodega'),
    ordering = ['name_bodega']


class ComatAdmin(admin.ModelAdmin):
    ordering = ['id_stdf']
    autocomplete_fields = ['id_bodega']






# Register your models here.
admin.site.register(Estado)
admin.site.register(Ubicacion)
admin.site.register(User)
admin.site.register(Uom)
admin.site.register(Owner)
admin.site.register(Ficha)
admin.site.register(Condicion)
admin.site.register(Clasificacion)
admin.site.register(Bodega , BodegaAdmin )
admin.site.register(Origen)
admin.site.register(Comat , ComatAdmin)
admin.site.register(Incoming)
admin.site.register(Consumos)
admin.site.register(Categotia_incoming)

