from django.contrib import admin
from .models import Temporada, Descarga, Bloc, Contacto

# Register your models here.
class TemporadaAdmin(admin.ModelAdmin):
    list_display=('video', 'titulo', 'descripcion')
    readonly_fields=("creado", "actualizado")

class DescargaAdmin(admin.ModelAdmin):
    list_display=('imagen', 'titulo', 'descripcion')
    readonly_fields=("creado", "actualizado")
    
class BlocAdmin(admin.ModelAdmin):
    list_display=('imagen', 'titulo', 'descripcion')
    readonly_fields=("creado", "actualizado")



admin.site.register(Temporada, TemporadaAdmin)
admin.site.register(Descarga, DescargaAdmin)
admin.site.register(Bloc, BlocAdmin)
admin.site.register(Contacto)