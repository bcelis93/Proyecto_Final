from django.contrib import admin

# Register your models here.
from mensajes.models import Mensaje, Blog, Autor

admin.site.register(Autor)
admin.site.register(Blog)
admin.site.register(Mensaje)
