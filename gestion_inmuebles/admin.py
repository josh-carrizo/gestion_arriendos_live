from datetime import timezone
from django.contrib import admin
from .models import Inmueble, Region, Comuna, Perfil

@admin.register(Inmueble)
class Inmueble_admin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'precio_mensual', 'comuna', 'tipo_inmueble')
    search_fields = ('nombre', 'direccion', 'comuna__nombre_comuna', 'tipo_inmueble')
    list_filter = ('tipo_inmueble', 'comuna', 'precio_mensual')
    readonly_fields =('fecha_creacion','ultima_modificacion')
    
    # def save_model(self, request, obj, form, change):
    #     if change:
    #         obj.ultima_modificacion = timezone.now()
    #     else:
    #         obj.fecha_creacion = timezone.now()
    #         obj.save()

@admin.register(Region)
class Region_admin(admin.ModelAdmin):
    list_display = ('nombre_region', 'numero_region')
    search_fields = ('nombre_region',)
    list_filter = ('numero_region',)

@admin.register(Comuna)
class Comuna_admin(admin.ModelAdmin):
    list_display = ('nombre_comuna', 'codigo_postal', 'region')
    search_fields = ('nombre_comuna', 'codigo_postal', 'region__nombre_region')
    list_filter = ('region',)

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):  
    list_display = ('nombres', 'apellidos', 'rut', 'tipo_usuario', 'comuna')
    search_fields = ('nombres', 'apellidos', 'rut', 'tipo_usuario')
    list_filter = ('tipo_usuario', 'comuna')    


# Registrar los modelos con admin.site.register()
# admin.site.register(Inmueble, Inmueble_admin)
# admin.site.register(Region, Region_admin)
# admin.site.register(Comuna, Comuna_admin)
# admin.site.register(Perfil, PerfilAdmin)