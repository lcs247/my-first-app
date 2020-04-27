from django.contrib import admin
from redflags.Apps.Videos.models import Ubicacion

# Register your models here.

class UbicacionRegistro (admin.ModelAdmin):
    list_display = ["nombre","direccion","nro_personas","tipo_apoyo","estado","modificado"]
    list_filter = ["estado","tipo_apoyo"]
    search_fields = ["nombre"]
    list_editable = ["estado"]
    class Meta:
        model = Ubicacion
        ordering = ["ingresado"]

admin.site.register(Ubicacion,UbicacionRegistro)

