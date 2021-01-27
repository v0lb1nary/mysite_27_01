from django.contrib import admin
from .models import *

#usado para adicionar o blog no site de administração
@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'rotulo', 'autor', 'data_publicacao', 'status')
    list_filter = ('status', 'data_criacao', 'data_publicacao', 'autor')
    search_fields = ('titulo', 'mensagem')
    date_hierarchy = ('data_publicacao')
    ordering = ('status', 'data_publicacao')
    prepopulated_fields = {'rotulo':('titulo',)}
    raw_id_fields = ('autor',)


@admin.register(Comentario)
class ComentariosAdmin(admin.ModelAdmin):
    '''Admin View for Comentarios'''

    list_display = ('nome','email')
    list_filter = ('ativo','data_criacao',)

    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    search_fields = ('nome','email')
    # date_hierarchy = ''
    # ordering = ('',)