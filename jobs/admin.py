from django.contrib import admin

from .models import Tarefa, Alarme, Grupo

admin.site.register(Tarefa)
admin.site.register(Alarme)
admin.site.register(Grupo)
