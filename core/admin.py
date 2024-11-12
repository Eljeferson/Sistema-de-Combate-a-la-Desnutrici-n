from django.contrib import admin
from .models import Disponibilidad, Voluntario, Donacion, Informante, Reporte
# Register your models here.

#DETALLA EN EL CASO SE NECESIT
#class DisponibilidadAdmin(admin.ModelAdmin):
#    list_display = ()

admin.site.register(Disponibilidad)
admin.site.register(Voluntario)
admin.site.register(Donacion)
admin.site.register(Informante)
admin.site.register(Reporte)