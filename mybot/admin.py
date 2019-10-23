from django.contrib import admin
from .models import Colaboradores,Ensino_dialogo,Comunicado_geral


@admin.register(Colaboradores)
class Colaboradores(admin.ModelAdmin):
    list_display = ['nome','email']


@admin.register(Ensino_dialogo)
class Ensino_dialogo(admin.ModelAdmin):
    list_display = ['pergunta', 'resposta','aprovado','data']

@admin.register(Comunicado_geral)
class Comunicado_geral(admin.ModelAdmin):
    list_display =['mensagem','data_envio','hora_envio','periodo']

